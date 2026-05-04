from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    amount: float

class TransactionOut(BaseModel):
    id: int
    acc_id: int
    type: str
    amount: float
    timestamp: datetime

    class Config:
        from_attributes = True

class WithdrawOut(BaseModel):
    transaction: TransactionOut
    balance: float

class DepositOut(BaseModel):
    transaction: TransactionOut
    balance: float