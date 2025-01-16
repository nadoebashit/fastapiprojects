from typing import List,Optional
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    quantity: int

class Order(BaseModel):
    id: Optional[int] = None
    customer_name: str
    status: str
    total_price: float
    products: List[Product]

class Metrics(BaseModel):
    request_count: int
    request_latency: float