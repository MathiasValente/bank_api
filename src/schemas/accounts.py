from pydantic import BaseModel

from src.schemas.transaction import TransactionOut

class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: float

    class Config:
        from_attributes = True


class AccountStatementOut(BaseModel):
    account_data: AccountOut
    transactions: list[TransactionOut]