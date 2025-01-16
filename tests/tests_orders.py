import base64
import pytest
from fastapi.testclient import TestClient
from main import app  # Замените на ваш модуль приложения

client = TestClient(app)

sample_order_data = {
    'customer_id': 123,
    'item_id': 1,
    'quantity': 2,
    'shipping_address': '123 Test St, Test City, TX'
}

def get_basic_auth_header(username, password):
    credentials = f"{username}:{password}"
    b64_credentials = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {b64_credentials}"}

def test_create_order():
    headers = get_basic_auth_header("admin", "admin123")  # Используйте корректные учетные данные
    response = client.post("/orders", json=sample_order_data, headers=headers)
    assert response.status_code == 201  # Проверка на успешное создание заказа

def test_create_order_invalid_data():
    invalid_order_data = {
        "item_id": "invalid",  # Некорректный тип данных
        "quantity": -1,        # Негативное значение
        "customer_id": 123,
        "shipping_address": ""
    }
    headers = get_basic_auth_header("admin", "admin123")  # Используйте корректные учетные данные
    response = client.post("/orders", json=invalid_order_data, headers=headers)
    assert response.status_code == 400  # Ожидаем ошибку 400 Bad Request