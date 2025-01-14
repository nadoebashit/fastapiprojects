class OrderEvent:
    def __init__(self, order_id: int, old_status: str, new_status: str):
        self.order_id = order_id
        self.old_status = old_status
        self.new_status = new_status

    def trigger(self):
        print(f"Событие: Заказ {self.order_id} изменён с {self.old_status} на {self.new_status}")
