"""
Решение задачи https://stepik.org/lesson/1798961/step/14
Оформляя каждый ендпоинт в отдельную функцию мы получаем copy-paste (унифицированный) код без лишнего
переименования переменных.
Который удобно сворачивать/разворачивать в текстовых редакторах.
А еще лучше - хранить в отдельных от сценария файлах, сгруппировав по бизнес-функцональности эндпоинтов.
PS: Этому миру не хватает встроенного логирования.
"""

import json
import httpx
import time

DEFAULT_TIMEOUT = 20    # без этого не работает на моем компьютере


def create_user() -> str | None:
    """Создает пользователя с email "user.{timestamp}@example.com"
    Возвращает userID.
    """
    url = "http://localhost:8003/api/v1/users"
    # Данные для создания пользователя 
    body = {
        "email": f"user.{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"
    }

    try:
        resp = httpx.post(url, json=body)
        data = resp.json()

        # Выводим полученные данные пользователя
        # print("Status Code:", resp.status_code)
        # print("Create user response:", data)

        user_id = data["user"]["id"]
        return user_id
    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса {url}: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Ошибка JSON {url}: {e}")

def create_account(user_id: str) -> tuple[str] | None:
    """Создание кошелька по user_id.
    Возвращает (account_id, card_id).
    """
    url = "http://localhost:8003/api/v1/accounts/open-credit-card-account"
    body = {
        "userId": user_id
    }
    try:
        resp = httpx.post(url, json=body, timeout=DEFAULT_TIMEOUT)
        # print("Status Code:", resp.status_code)
        
        data = resp.json()
        # print("Create account response:", data)
        
        return data['account']['id'], data['account']['cards'][0]['id']
    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса {url}: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Ошибка JSON {url}: {e}")
        print(resp.text)
        print(resp.request.content)

def make_purchase_operation(account_id: str, card_id: str) -> str | None:
    """Покупка. account_id и card_id - заданы, остальные параметры пока захардкожены.
    Возвращает operation_id.
    """
    url = "http://localhost:8003/api/v1/operations/make-purchase-operation"
    body = {
          "status": "IN_PROGRESS",
          "amount": 77.99,
          "cardId": card_id,
          "accountId": account_id,
          "category": "taxi"
        }
    try:
        resp = httpx.post(url, json=body, timeout=DEFAULT_TIMEOUT)
        # print("Status Code:", resp.status_code)
        
        data = resp.json()
        # print("Purchase response:", data)
        
        return resp.json()['operation']['id']
    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса {url}: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Ошибка JSON {url}: {e}")
        
def get_operation_receipt(operation_id: str):
    """Чек по operation_id.
    """
    url = f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}"
    
    try:
        resp = httpx.get(url, timeout=DEFAULT_TIMEOUT)
        # print("Status Code:", resp.status_code)
        # print("Request:", resp.request.url)
        
        data = resp.json()
        print("Receipt response:", data)

    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса {url}: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Ошибка JSON {url}: {e}")


if __name__ == "__main__":
    user_id = create_user()
    account_id, card_id = create_account(user_id)
    operation_id = make_purchase_operation(account_id, card_id)
    get_operation_receipt(operation_id)
