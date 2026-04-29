from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.db import Base

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True)
    
    user_id: Mapped[int] = mapped_column(Integer,
                                         ForeignKey("users.id"),
                                         nullable=False)
    
    balance: Mapped[float] = mapped_column(Float,
                                           nullable=False,
                                           default=0)
    
    user = relationship("User", back_populates="accounts")
    
    transactions = relationship("Transaction",
                                back_populates="account",
                                cascade="all, delete-orphan")