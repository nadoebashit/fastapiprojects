from sqlalchemy.orm import Session
from infrastructure.repositories.order_repository import OrderRepository

class OrderService:
    @staticmethod
    def create_order(db: Session, order_data: dict, user_role: str):
        if user_role not in ["User", "Admin"]:
            raise PermissionError("Доступ запрещён")
        return OrderRepository.create_order(db, order_data)

    @staticmethod
    def get_orders(db: Session, filters: dict = None):
        return OrderRepository.get_orders(db, filters)

    @staticmethod
    def update_order(db: Session, order_id: int, updates: dict, user_role: str):
        order = OrderRepository.update_order(db, order_id, updates)
        if not order:
            raise ValueError("Заказ не найден")
        return order

    @staticmethod
    def soft_delete_order(db: Session, order_id: int, user_role: str):
        if user_role != "Admin":
            raise PermissionError("Удаление разрешено только администратору")
        OrderRepository.soft_delete_order(db, order_id)
