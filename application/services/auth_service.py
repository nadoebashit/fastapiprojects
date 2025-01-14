class AuthService:
    @staticmethod
    def login(username: str, password: str) -> str:
        # Упрощённая авторизация
        if username == "admin" and password == "admin":
            return "admin_token"
        elif username == "user" and password == "user":
            return "user_token"
        raise ValueError("Неверные учётные данные")

    @staticmethod
    def verify_token(token: str) -> str:
        if token == "admin_token":
            return "Admin"
        elif token == "user_token":
            return "User"
        raise PermissionError("Неверный токен")
