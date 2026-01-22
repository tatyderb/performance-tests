from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationResponseDict(TypedDict):
    operation: OperationDict

class OperationReceiptDict(TypedDict):
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class OperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict

class GetOperationsQueryDict(TypedDict):
    accountId: str

class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]

class MakeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    pass

class MakeWithdawalOperationRequestDict(MakeOperationRequestDict):
    pass

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    category: str

class MakeFeeOperationResponseDict(OperationResponseDict):
    pass

class MakeTopUpOperationResponseDict(OperationResponseDict):
    pass

class MakeCashbackOperationResponseDict(OperationResponseDict):
    pass

class MakeTransferOperationResponseDict(OperationResponseDict):
    pass

class MakeBillPaymentOperationResponseDict(OperationResponseDict):
    pass

class MakeWithdawalOperationResponseDict(OperationResponseDict):
    pass

class MakePurchaseOperationResponseDict(OperationResponseDict):
    pass

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос создания операции комиссии.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос создания операции пополнения.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос создания операции кэшбека.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос создания операции перевода.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос создания операции покупки.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос создания операции оплаты по счету.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeWithdawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос создания операции снятия наличных.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> OperationResponseDict:
        """
        Получение информации по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект OperationResponseDict).
        """
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> OperationReceiptDict:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект OperationReceiptDict).
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получение списка операций для определенного счета.

        :param account_id: Id счета.
        :return: Ответ от сервера (объект GetOperationsResponseDict).
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> OperationsSummaryResponseDict:
        """
        Получение статистики по операциям для определенного счета.

        :param account_id: Id счета
        :return: Ответ от сервера (объект OperationsSummaryResponseDict).
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Операции пополнения.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeTopUpOperationResponseDict с результатом операции.
        """
        body = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(body)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Операция кэшбека.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeCashbackOperationResponseDict с результатом операции.
        """
        body = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(body)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Операция перевода.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeTransferOperationResponseDict с результатом операции.
        """
        body = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(body)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """
        Операция покупки.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakePurchaseOperationResponseDict с результатом операции.
        """
        body = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="taxi"
        )
        response = self.make_purchase_operation_api(body)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Оплата по счету.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeBillPaymentOperationResponseDict с результатом операции.
        """
        body = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(body)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeWithdawalOperationResponseDict:
        """
        Выполняет POST-запрос создания операции снятия наличных.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeWithdawalOperationResponseDict с результатом операции.
        """
        body = MakeWithdawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(body)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
