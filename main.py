from fastapi import FastAPI
from infrastructure.logging_config import setup_logging
from presentation.routes import auth, orders
from infrastructure.database import engine
from domain.models import Base

# Создаем экземпляр приложения
app = FastAPI()

# Настройка логирования
setup_logging()

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# Пример обработчика для проверки статуса сервера
@app.get("/")
def read_root():
    return {"status": "Server is running"}
