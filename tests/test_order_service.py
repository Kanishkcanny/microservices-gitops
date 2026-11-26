
import importlib.util
from pathlib import Path

import httpx
from fastapi.testclient import TestClient

module_path = (
    Path(__file__).parent.parent
    / "services/order-service/main.py"
)

spec = importlib.util.spec_from_file_location(
    "order_service", module_path
)
order_service = importlib.util.module_from_spec(spec)
spec.loader.exec_module(order_service)

client = TestClient(order_service.app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "service": "order-service",
        "status": "running"
    }


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_all_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_existing_order():
    response = client.get("/orders/101")
    assert response.status_code == 200
    assert response.json()["product"] == "Laptop"


def test_get_nonexistent_order():
    response = client.get("/orders/999")
    assert response.status_code == 404


def test_order_details_with_user(monkeypatch):
    def mock_user_service(*args, **kwargs):
        return httpx.Response(
            200,
            json={
                "id": 1,
                "name": "Kanishka",
                "email": "kanishka@example.com"
            },
            request=httpx.Request("GET", "http://user-service/users/1")
        )

    monkeypatch.setattr(
        order_service.httpx,
        "get",
        mock_user_service
    )

    response = client.get("/orders/101/details")

    assert response.status_code == 200
    assert response.json()["order"]["product"] == "Laptop"
    assert response.json()["user"]["name"] == "Kanishka"


def test_order_details_when_user_not_found(monkeypatch):
    def mock_user_service(*args, **kwargs):
        return httpx.Response(
            404,
            json={"detail": "User not found"},
            request=httpx.Request("GET", "http://user-service/users/1")
        )

    monkeypatch.setattr(
        order_service.httpx,
        "get",
        mock_user_service
    )

    response = client.get("/orders/101/details")

    assert response.status_code == 404
    assert response.json()["detail"] == (
        "User associated with this order was not found"
    )
