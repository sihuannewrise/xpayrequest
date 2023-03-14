from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class PaymentProcessing(Base):
    pr_id: Mapped[int] = mapped_column(ForeignKey('paymentrequest.id'))
    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'))
    verdict: Mapped[str]
    processed_at: Mapped[datetime]
