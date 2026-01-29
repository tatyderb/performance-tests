from enum import StrEnum

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"


class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"


# Добавили описание структуры счета
class AccountSchema(BaseModel):
    """
    Описание структуры аккаунта.
    """
    id: str
    type: AccountType
    # Вложенный объект для списка карт привязанных к счету
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """
    Структура данных для получения списка счетов пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    user_id: str

class GetAccountsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка счетов.
    """
    accounts: list[AccountSchema]

class OpenBaseAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия счета (родительская схема).
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    user_id: str

class OpenBaseAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа открытия счета (родительская схема).
    """
    account: AccountSchema


class OpenDepositAccountRequestSchema(OpenBaseAccountRequestSchema):
    """
    Структура данных для открытия депозитного счета.
    """

class OpenDepositAccountResponseSchema(OpenBaseAccountResponseSchema):
    """
    Описание структуры ответа открытия депозитного счета.
    """

class OpenSavingsAccountRequestSchema(OpenBaseAccountRequestSchema):
    """
    Структура данных для открытия сберегательного счета.
    """

class OpenSavingsAccountResponseSchema(OpenBaseAccountResponseSchema):
    """
    Описание структуры ответа открытия сберегательного счета.
    """

class OpenDebitCardAccountRequestSchema(OpenBaseAccountRequestSchema):
    """
    Структура данных для открытия дебетового счета.
    """

class OpenDebitCardAccountResponseSchema(OpenBaseAccountResponseSchema):
    """
    Описание структуры ответа открытия дебетового счета.
    """

class OpenCreditCardAccountRequestSchema(OpenBaseAccountRequestSchema):
    """
    Структура данных для открытия кредитного счета.
    """

class OpenCreditCardAccountResponseSchema(OpenBaseAccountResponseSchema):
    """
    Описание структуры ответа открытия кредитного счета.
    """
