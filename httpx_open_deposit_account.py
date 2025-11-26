"""
Решение задачи https://stepik.org/lesson/1798960/step/16
1. Будет логирование - исчезнут закоментаренные print
2. когда-то добавится обработка ошибок
"""

import httpx  # Импортируем библиотеку HTTPX
import time


DEFAULT_HOST = "localhost:8003"
host = DEFAULT_HOST

def url(url: str)-> str:
    """Добавляет хост к ендпоинту."""
    return "https://" + host + url

def create_user() -> str | None:
    """Создает пользователя с email "user.{timestamp}@example.com"
    Возвращает userID.
    """
    # _url = url("/api/v1/users")
    _url = "http://localhost:8003/api/v1/users"
    # Данные для создания пользователя 
    body = {
        "email": f"user.{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"
    }

    # Выполняем запрос на создание пользователя
    try:
        resp = httpx.post(_url, json=body)
        data = resp.json()

        # Выводим полученные данные пользователя
        print("Status Code:", resp.status_code)
        print("Create user response:", data)

        user_id = data["user"]["id"]
        return user_id
    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса: {e}")

def create_account(user_id: str) -> str | None:
    """Создание кошелька по user_id.
    Возвращает account_id.
    """
    # _url = url("/api/v1/accounts/open-deposit-account")
    _url = "http://localhost:8003/api/v1/accounts/open-deposit-account"
    body = {
        "userId": user_id
    }
    try:
        resp = httpx.post(_url, json=body, timeout=10)
        print("Status Code:", resp.status_code)
        
        data = resp.json()
        print("Create account response:", data)
        
        return resp.json()['account']['id']
    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса: {e}")


if __name__ == "__main__":
    user_id = create_user()
    create_account(user_id)
