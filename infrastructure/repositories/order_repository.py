from sqlalchemy.orm import Session
from domain.models import Order, Product

class OrderRepository:
    @staticmethod
    def create_order(db: Session, order_data: dict):
        order = Order(
            customer_name=order_data["customer_name"],
            status=order_data["status"],
            total_price=order_data["total_price"]
        )
        db.add(order)
        db.commit()
        db.refresh(order)

        # Добавление продуктов
        for product_data in order_data["products"]:
            product = Product(**product_data, order_id=order.order_id)
            db.add(product)
        db.commit()
        return order

    @staticmethod
    def get_orders(db: Session, filters: dict = None):
        query = db.query(Order)
        if filters:
            if "status" in filters:
                query = query.filter(Order.status == filters["status"])
            if "min_price" in filters:
                query = query.filter(Order.total_price >= filters["min_price"])
            if "max_price" in filters:
                query = query.filter(Order.total_price <= filters["max_price"])
        return query.all()

    @staticmethod
    def update_order(db: Session, order_id: int, updates: dict):
        order = db.query(Order).filter(Order.order_id == order_id).first()
        if not order:
            return None

        for key, value in updates.items():
            setattr(order, key, value)
        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    def soft_delete_order(db: Session, order_id: int):
        order = db.query(Order).filter(Order.order_id == order_id).first()
        if order:
            order.status = "deleted"
            db.commit()
