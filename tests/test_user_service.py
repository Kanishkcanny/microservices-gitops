
import importlib.util
from pathlib import Path
from fastapi.testclient import TestClient

module_path = Path(__file__).parent.parent / "services/user-service/main.py"
spec = importlib.util.spec_from_file_location("user_service", module_path)
user_service = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user_service)

client = TestClient(user_service.app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "service": "user-service",
        "status": "running"
    }


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "user-service"
    }


def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_existing_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Kanishka"


def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
