from domain.models import Order
from infrastructure.database import db
from application.services.metrics_service import MetricsService
from prometheus_client import Counter, Histogram
import time  # Для измерения времени выполнения


class OrderService:
    @staticmethod
    def create_order(order_data: dict, user: dict):
        start_time = time.time()

        # Генерация уникального order_id
        if "id" not in order_data:
            order_data["id"] = len(db["orders"]) + 1  # Автоинкремент

        order = Order(**order_data)
        db["orders"].append(order.dict())

        duration = time.time() - start_time
        MetricsService.record_request(endpoint="/orders", method="POST", status=200)
        MetricsService.record_latency(endpoint="/orders", duration=duration)

        return order, {"message": "Order created successfully.", "user": user}

    @staticmethod
    def get_orders(filters: dict, user: dict):
        start_time = time.time()

        orders = db["orders"]
        if filters.get("status"):
            orders = [o for o in orders if o["status"] == filters["status"]]
        if filters.get("min_price"):
            orders = [o for o in orders if o["total_price"] >= filters["min_price"]]
        if filters.get("max_price"):
            orders = [o for o in orders if o["total_price"] <= filters["max_price"]]

        duration = time.time() - start_time
        MetricsService.record_request(endpoint="/orders", method="GET", status=200)
        MetricsService.record_latency(endpoint="/orders", duration=duration)

        # Возврат заказов с видимым order_id
        return {"orders": orders, "message": "Orders retrieved successfully."}

    @staticmethod
    def update_order(order_id: int, user: dict):
        start_time = time.time()
        order = db["orders"]
        duration = time.time() - start_time
        MetricsService.record_request(endpoint="/orders", method="POST", status=200)
        MetricsService.record_latency(endpoint="/orders", duration=duration)
        return order
    
    @staticmethod
    def get_order_by_id(order_id: int, user: dict):
        start_time = time.time()

        for order in db["orders"]:
            if order["id"] == order_id:
                duration = time.time() - start_time
                MetricsService.record_request(endpoint=f"/orders/{order_id}", method="GET", status=200)
                MetricsService.record_latency(endpoint=f"/orders/{order_id}", duration=duration)

                return order, {"message": "Order retrieved successfully."}

        MetricsService.record_request(endpoint=f"/orders/{order_id}", method="GET", status=404)
        return None, {"message": "Order not found."}

    @staticmethod
    def soft_delete_order(order_id: int, user: dict):
        start_time = time.time()

        for order in db["orders"]:
            if order["id"] == order_id:
                order["deleted"] = True

                duration = time.time() - start_time
                MetricsService.record_request(endpoint=f"/orders/{order_id}", method="DELETE", status=200)
                MetricsService.record_latency(endpoint=f"/orders/{order_id}", duration=duration)

                return {"message": "Order softly deleted"}

        MetricsService.record_request(endpoint=f"/orders/{order_id}", method="DELETE", status=404)
        return None, {"message": "Order not found."}
