import httpx
import time

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']

# Создать кредитный счёт для пользователя
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json = {"userId": user_id}
)
credit_card_account_json = open_credit_card_account_response.json()
account_id = credit_card_account_json["account"]["id"]
card_id = credit_card_account_json["account"]["cards"][0]["id"]

# Покупка
pushcase_body = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": card_id,
  "accountId": account_id,
  "category": "taxi"
}
pushcase_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=pushcase_body)
operation_id = pushcase_response.json()["operation"]["id"]

# чек по операции
receipt_doc_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")
receipt_data = receipt_doc_response.json()
print(receipt_data)