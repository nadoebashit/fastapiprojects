from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class OrderCreate(BaseModel):
    customer_name: str
    status: str
    products: List[ProductCreate]

class OrderResponse(OrderCreate):
    order_id: str

class OrderUpdate(BaseModel):
    status: Optional[str]
    products: Optional[List[ProductCreate]]

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
