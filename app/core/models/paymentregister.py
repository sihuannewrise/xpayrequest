from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.db import Base


class PaymentRegister(Base):
    pr_id = Column(Integer, ForeignKey('paymentrequest.id'), nullable=False)
    payment_status = Column(Integer, ForeignKey('paymentstatus.id'), nullable=False)
    fulfilled_date = Column(DateTime)
