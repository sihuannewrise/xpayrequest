from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime

from app.core.db import Base

class PaymentRequests(Base):
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
