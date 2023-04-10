from typing import Optional, List

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.models._common import EntityBase
from app.core.models._selectchoice import BankOPFType


class Bank(EntityBase):
    bic: Mapped[str] = mapped_column(String(9), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(160))
    correspondent_account: Mapped[Optional[str]] = mapped_column(String(20))
    payment_city: Mapped[Optional[str]] = mapped_column(String(50))

    swift: Mapped[Optional[str]] = mapped_column(String(11))
    registration_number: Mapped[Optional[str]] = mapped_column(String(20))
    treasury_accounts: Mapped[Optional[str]] = mapped_column(String(20))
    opf_type: Mapped[Optional[BankOPFType]]
    kpp: Mapped[Optional[str]] = mapped_column(String(9), index=True)

    __table_args__ = (
        UniqueConstraint('inn', 'kpp', name='_bank_inn_kpp_unique'),)

    accounts: Mapped[List['BankAccount']] = relationship(backref='bank')
