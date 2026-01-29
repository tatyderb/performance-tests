from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema,
    MakeFeeOperationRequestSchema,
    MakeTopUpOperationRequestSchema,
    MakeCashbackOperationRequestSchema,
    MakeTransferOperationRequestSchema,
    MakePurchaseOperationRequestSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeWithdawalOperationRequestSchema,
    OperationResponseSchema,
    OperationReceiptSchema,
    GetOperationsResponseSchema,
    OperationsSummaryResponseSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeWithdawalOperationResponseSchema, OperationStatus
)


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

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос создания операции комиссии.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос создания операции пополнения.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос создания операции кэшбека.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос создания операции перевода.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос создания операции покупки.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос создания операции оплаты по счету.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeWithdawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос создания операции снятия наличных.

        :param request: Словарь данными для операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> OperationResponseSchema:
        """
        Получение информации по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект OperationResponseSchema).
        """
        response = self.get_operation_api(operation_id=operation_id)
        return OperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> OperationReceiptSchema:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект OperationReceiptSchema).
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return OperationReceiptSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получение списка операций для определенного счета.

        :param account_id: Id счета.
        :return: Ответ от сервера (объект GetOperationsResponseSchema).
        """
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> OperationsSummaryResponseSchema:
        """
        Получение статистики по операциям для определенного счета.

        :param account_id: Id счета
        :return: Ответ от сервера (объект OperationsSummaryResponseSchema).
        """
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return OperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """
        Операции пополнения.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeTopUpOperationResponseSchema с результатом операции.
        """
        body = MakeTopUpOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(body)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        Операция кэшбека.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeCashbackOperationResponseSchema с результатом операции.
        """
        body = MakeCashbackOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(body)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        Операция перевода.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeTransferOperationResponseSchema с результатом операции.
        """
        body = MakeTransferOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(body)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """
        Операция покупки.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakePurchaseOperationResponseSchema с результатом операции.
        """
        body = MakePurchaseOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id,
            category="taxi"
        )
        response = self.make_purchase_operation_api(body)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        Оплата по счету.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeBillPaymentOperationResponseSchema с результатом операции.
        """
        body = MakeBillPaymentOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(body)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeWithdawalOperationResponseSchema:
        """
        Выполняет POST-запрос создания операции снятия наличных.

        :param card_id: Id карты
        :param account_id: Id счета
        :return: Объект MakeWithdawalOperationResponseSchema с результатом операции.
        """
        body = MakeWithdawalOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(body)
        return MakeWithdawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
