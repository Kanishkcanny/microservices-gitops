from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="User Service",
    description="User management microservice",
    version="1.0.0"
)

class User(BaseModel):
    id: int
    name: str
    email: str

users = [
    User(id=1, name="Kanishka", email="kanishka@example.com"),
    User(id=2, name="Rahul", email="rahul@example.com")
]

@app.get("/")
def root():
    return {"service": "user-service", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "user-service"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
