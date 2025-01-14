def verify_token(token: str):
    if token == "mock_token":
        return {"username": "mock_user"}
    raise Exception("Invalid token")
