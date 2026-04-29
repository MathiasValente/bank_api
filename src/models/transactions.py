from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.db import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True)
    
    acc_id: Mapped[int] = mapped_column(Integer,
                                        ForeignKey("accounts.id"),
                                        nullable=False)
    
    type: Mapped[str] = mapped_column(String(255),
                                      nullable=False)
    
    amount: Mapped[float] = mapped_column(Float,
                                          nullable=False)
    
    timestamp: Mapped[str] = mapped_column(String(255),
                                           nullable=False)
    
    account = relationship("Account", back_populates="transactions")