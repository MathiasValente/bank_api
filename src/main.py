from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database.init_db import init_models
from src.routes.auth import router as auth_route
from src.routes.user import router as user_route
from src.routes.accounts import router as acc_route
from src.routes.transactions import router as transactions_route
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_route)
app.include_router(auth_route)
app.include_router(acc_route)
app.include_router(transactions_route)