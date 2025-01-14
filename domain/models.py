from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.database import Base

# Таблица Product
class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.order_id"))

# Таблица Order
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)

    # Связь с продуктами
    products = relationship("Product", backref="order", cascade="all, delete")
