from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class PaymentRegister(Base):
    fulfill_date: Mapped[Optional[datetime]]
    pr_id: Mapped[int] = mapped_column(ForeignKey('paymentrequest.id'))

    status_id: Mapped[int] = mapped_column(ForeignKey('paymentstatus.id'))
    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'))

    status: Mapped['PaymentStatus'] = relationship(
        backref='paymentregister')

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__} '
            f'<register_id {self.id}, pr_id {self.pr_id}>'
        )
