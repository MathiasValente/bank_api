from src.database.db import engine, Base
from src.models import users, accounts, transactions

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)