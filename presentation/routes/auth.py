from fastapi import APIRouter
from application.services.auth_service import AuthService

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    return {"access_token": AuthService.login(username, password)}
