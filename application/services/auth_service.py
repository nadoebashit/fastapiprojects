from fastapi import HTTPException
from infrastructure.database import users_db

class AuthService:
    db = {
    "orders": []
    }

    users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    }

    @staticmethod
    def verify_user(username: str, password: str):
        user = AuthService.users_db.get(username)
        if user and user["password"] == password:
            return {"username": username, "role": user["role"]}
        return None

    
