from sqlalchemy import select

from fastapi import HTTPException, status

from src.models.accounts import Account

async def get_user_account(user_id: int,
                           account_id: int,
                           db):
    stmt = select(Account).where(Account.user_id == user_id,
                                 Account.id == account_id)
    
    result = await db.execute(stmt)
    account = result.scalar_one_or_none()

    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Account not found!")
    
    return account