from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardStatus(StrEnum):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class CardPaymentSystem(StrEnum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"


class CardSchema(BaseModel):
    """
    Описание структуры карты.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: date
    payment_system: CardPaymentSystem


class IssueVirtualCardRequestSchema(BaseModel):
    """
    Структура данных для выпуска виртуальной карты.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)

    user_id: str
    account_id: str


class IssueVirtualCardResponseSchema(BaseModel):
    """
    Описание структуры ответа выпуска виртуальной карты.
    """
    card: CardSchema


class IssuePhysicalCardRequestSchema(BaseModel):
    """
    Структура данных для выпуска физической карты.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)

    user_id: str
    account_id: str


class IssuePhysicalCardResponseSchema(BaseModel):
    """
    Описание структуры ответа выпуска физической карты.
    """
    card: CardSchema
