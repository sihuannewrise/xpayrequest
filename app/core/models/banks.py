from sqlalchemy import Column, DateTime, Integer, String

from app.core.db import Base


class Banks(Base):
    bic = Column(Integer(), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    city = Column(String(150), nullable=False)
    correspondent_account = 
