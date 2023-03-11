from typing import Optional
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class BankAccount(Base):
    account: Mapped[str] = mapped_column(String(20))
    currency: Mapped[str] = mapped_column(String(20))
    bank_id: Mapped[int] = mapped_column(ForeignKey('bank.id'))
    ca_id: Mapped[int] = mapped_column(ForeignKey('counteragent.id'),)
    type_id: Mapped[int] = mapped_column(ForeignKey('bankaccounttype.id'))
    is_default: Mapped[Optional[bool]]

    __table_args__ = (UniqueConstraint(
        'account', 'bank_id', name='_account_bank_unique',
    ),)

    bank: Mapped['Bank'] = relationship(backref='bankaccount')
