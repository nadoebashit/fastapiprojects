from fastapi import APIRouter, Depends, Query
from application.services.order_service import OrderService
from application.services.auth_service import AuthService
from presentation.dtos import OrderCreate, OrderUpdate
from typing import List

router = APIRouter()

@router.post("/")
def create_order(order: OrderCreate, token: str = Depends(AuthService.verify_token)):
    user_role = AuthService.verify_token(token)
    return OrderService.create_order(order.dict(), user_role)

@router.get("/")
def get_orders(
    status: str = Query(None),
    min_price: float = Query(None),
    max_price: float = Query(None),
):
    filters = {"status": status, "min_price": min_price, "max_price": max_price}
    return OrderService.get_orders(filters)

@router.put("/{order_id}")
def update_order(order_id: int, updates: OrderUpdate, token: str = Depends(AuthService.verify_token)):
    user_role = AuthService.verify_token(token)
    return OrderService.update_order(order_id, updates.dict(), user_role)

@router.delete("/{order_id}")
def soft_delete_order(order_id: int, token: str = Depends(AuthService.verify_token)):
    user_role = AuthService.verify_token(token)
    OrderService.soft_delete_order(order_id, user_role)
    return {"message": "Заказ мягко удалён"}
