from datetime import datetime
from uuid import UUID
from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class PaymentProcessing(Base):
    pr_id: Mapped[int] = mapped_column(ForeignKey('paymentrequest.id'))
    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'))
    verdict_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('paymentverdict.id'))
    processed_at: Mapped[datetime]

    signor: Mapped[List['User']] = relationship(
        backref='proc')

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} ('
            f'proc_id={self.id}, pr_id={self.pr_id})>'
        )
