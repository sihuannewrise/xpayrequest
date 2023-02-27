from sqlalchemy import Column, DateTime, Integer, String

from app.core.db import Base


class Bank(Base):
    bic = Column(Integer(), nullable=False)
    name = Column(String(100), nullable=False)
    city = Column(String(150), nullable=False)
