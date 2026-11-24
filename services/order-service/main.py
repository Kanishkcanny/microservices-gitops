
import os
import httpx

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Order Service",
    description="Order management microservice",
    version="1.0.0"
)

USER_SERVICE_URL = os.getenv(
    "USER_SERVICE_URL",
    "http://localhost:8001"
)

class Order(BaseModel):
    id: int
    user_id: int
    product: str
    amount: float

orders = [
    Order(id=101, user_id=1, product="Laptop", amount=55000),
    Order(id=102, user_id=2, product="Keyboard", amount=1500)
]

@app.get("/")
def root():
    return {"service": "order-service", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "order-service"}

@app.get("/orders")
def get_orders():
    return orders

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/{order_id}/details")
def get_order_details(order_id: int):
    order = next(
        (item for item in orders if item.id == order_id),
        None
    )

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    try:
        response = httpx.get(
            f"{USER_SERVICE_URL}/users/{order.user_id}",
            timeout=5.0
        )
        response.raise_for_status()
        user = response.json()

    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="User associated with this order was not found"
            )
        raise HTTPException(status_code=502, detail="User Service error")

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="User Service is unavailable"
        )

    return {
        "order": order,
        "user": user
    }
