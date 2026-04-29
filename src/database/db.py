from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.core.config import database_settings


DB_URL = database_settings.DB_URL
engine = create_async_engine(url=DB_URL,
                             echo=True)

SessionLocal = sessionmaker(bind=engine,
                            class_=AsyncSession,
                            expire_on_commit=False)

Base = declarative_base()