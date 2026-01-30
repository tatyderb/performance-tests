from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_alias=True)
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str
    category: str
    created_at: str
    account_id: str

class OperationResponseSchema(BaseModel):
    operation: OperationSchema

class OperationReceiptSchema(BaseModel):
    url: str
    document: str

class OperationsSummarySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_alias=True)
    spent_amount: float
    received_amount: float
    cashback_amount: float

class OperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema

class GetOperationsQuerySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_alias=True)
    account_id: str

class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]

class MakeOperationRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    pass

class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    pass

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    pass

class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    pass

class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    pass

class MakeWithdawalOperationRequestSchema(MakeOperationRequestSchema):
    pass

class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    category: str = Field(default_factory=fake.category)

class MakeFeeOperationResponseSchema(OperationResponseSchema):
    pass

class MakeTopUpOperationResponseSchema(OperationResponseSchema):
    pass

class MakeCashbackOperationResponseSchema(OperationResponseSchema):
    pass

class MakeTransferOperationResponseSchema(OperationResponseSchema):
    pass

class MakeBillPaymentOperationResponseSchema(OperationResponseSchema):
    pass

class MakeWithdawalOperationResponseSchema(OperationResponseSchema):
    pass

class MakePurchaseOperationResponseSchema(OperationResponseSchema):
    pass

# account_id='ad3089ad-8b67-41a7-aa64-a93a0218347b'
# card_id='354b77c0-1874-4d28-8cb0-af8b386271f2'
# body = MakeTopUpOperationRequestSchema(
#     status=OperationStatus.COMPLETED,
#     amount=55.77,
#     card_id=card_id,
#     account_id=account_id
# )
# body = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
# print(body)