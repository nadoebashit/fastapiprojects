from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from application.services.order_service import OrderService
from application.services.auth_service import AuthService

router = APIRouter()
security = HTTPBasic()

def authenticate_user(
    credentials: HTTPBasicCredentials = Depends(security)
):
    # Проверка пользователя через AuthService
    user = AuthService.verify_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Неверные учетные данные")
    return user

@router.post("/")
def create_order(
    order: dict,
    user: dict = Depends(authenticate_user), 
):
    
    return OrderService.create_order(order, user)

@router.get("/")
def get_orders(
    status: str = Query(None),
    min_price: float = Query(None),
    max_price: float = Query(None),
    user: dict = Depends(authenticate_user),  
):
    # Фильтрация заказов
    filters = {"status": status, "min_price": min_price, "max_price": max_price}
    return OrderService.get_orders(filters, user)

@router.put("/{order_id}")
def update_order(
    order_id: int,
    updates: dict,
    user: dict = Depends(authenticate_user),  # Зависимость для аутентификации пользователя
):
    # Обновление заказа
    return OrderService.update_order(order_id, updates, user)

@router.delete("/{order_id}")
def soft_delete_order(
    order_id: int,
    user: dict = Depends(authenticate_user),  # Зависимость для аутентификации пользователя
):
    OrderService.soft_delete_order(order_id, user)
    return {"message": "Заказ мягко удалён"}
