from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status

from src.core.security import user_dependency

from src.services.account_service import get_user_account

from src.dependencies.db_dependency import db_dependency

from src.models.transactions import Transaction
from src.models.accounts import Account

from src.schemas.transaction import TransactionIn, WithdrawOut, DepositOut

router = APIRouter(prefix="/account/{account_id}",
                   tags=["transactions"])

@router.post("/deposit", response_model=DepositOut)
async def create_deposit(account_id: int,
                         transaction_to_create: TransactionIn,
                         user: user_dependency,
                         db: db_dependency):
    
    account = await get_user_account(user.id, account_id, db)

    deposit = Transaction(acc_id = account.id,
                          type = "deposit",
                          amount = transaction_to_create.amount,
                          timestamp = datetime.now(timezone.utc))
    
    db.add(deposit)

    account.balance += transaction_to_create.amount

    await db.commit()
    await db.refresh(deposit)

    return DepositOut(transaction=deposit,
                      balance=account.balance)
    

@router.post("/withdraw", response_model=WithdrawOut)
async def create_withdraw(account_id: int,
                          transaction_to_create: TransactionIn,
                          user: user_dependency,
                          db: db_dependency):
    
    account = await get_user_account(user.id, account_id, db)

    if transaction_to_create.amount > account.balance:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Withdraw amount greater than account balance")

    withdraw = Transaction(acc_id = account.id,
                           type = "withdraw",
                           amount = transaction_to_create.amount,
                           timestamp = datetime.now(timezone.utc))
    
    db.add(withdraw)

    account.balance -= transaction_to_create.amount
    
    await db.commit()
    await db.refresh(withdraw)

    return WithdrawOut(transaction=withdraw,
                       balance=account.balance)