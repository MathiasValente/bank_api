from sqlalchemy import select

from fastapi import HTTPException, status

from src.models.transactions import Transaction

async def get_all_transactions(acc_id: int, db):
    stmt = (select(Transaction)
            .where(Transaction.acc_id == acc_id)
            .order_by(Transaction.timestamp.desc()))
    
    result = await db.execute(stmt)
    transactions = result.scalars().all()

    if not transactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Transactions not found")

    return transactions