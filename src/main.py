from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database.init_db import init_models
from src.routes.auth import router as auth_route
from src.routes.user import router as user_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_route)
app.include_router(auth_route)