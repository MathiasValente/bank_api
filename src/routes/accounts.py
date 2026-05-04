from fastapi import APIRouter

from src.core.security import user_dependency

from src.dependencies.db_dependency import db_dependency

from src.services.account_service import get_user_account
from src.services.transactions_service import get_all_transactions

from src.models.accounts import Account
from src.schemas.accounts import AccountOut, AccountStatementOut

router = APIRouter(prefix="/user/account",
                   tags=["account"])

@router.post("/create", response_model=AccountOut)
async def create_account(user: user_dependency,
               db: db_dependency):
    account_created = Account(user_id = user.id,
                              balance = 0)
    db.add(account_created)
    await db.commit()
    await db.refresh(account_created)

    return account_created

@router.get("/{acc_id}/statement", response_model=AccountStatementOut)
async def get_account_statement(acc_id: int,
                                user: user_dependency,
                                db: db_dependency):
    
    account = await get_user_account(user.id, acc_id, db)
    transactions = await get_all_transactions(acc_id, db)

    return AccountStatementOut(account_data= account,
                               transactions= transactions)