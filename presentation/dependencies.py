from fastapi import Depends
from application.services.auth_service import verify_token

def get_current_user(token: str = Depends(verify_token)):
    return {"username": "mock_user"}  # Заглушка для проверки токена
