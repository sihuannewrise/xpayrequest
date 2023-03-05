from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class PaymentRegister(Base):
    pr_id: Mapped[int] = mapped_column(ForeignKey('paymentrequest.id'))
    payment_status: Mapped[int] = mapped_column(ForeignKey('paymentstatus.id'))
    fulfilled_date: Mapped[Optional[datetime]]
