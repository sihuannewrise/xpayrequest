from typing import Optional, List

from sqlalchemy import String, Index, and_
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.models._common import EntityBase
from app.core.models._selectchoice import BankOPFType


class Bank(EntityBase):
    bic: Mapped[str] = mapped_column(String(9), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(160))
    correspondent_account: Mapped[Optional[str]] = mapped_column(String(20))
    payment_city: Mapped[Optional[str]] = mapped_column(String(50))

    inn: Mapped[Optional[str]] = mapped_column(String(12))
    kpp: Mapped[Optional[str]] = mapped_column(String(9))

    swift: Mapped[Optional[str]] = mapped_column(String(11))
    registration_number: Mapped[Optional[str]] = mapped_column(String(20))
    treasury_accounts: Mapped[Optional[str]] = mapped_column(String(20))
    opf_type: Mapped[Optional[BankOPFType]] = mapped_column(String(20))

    __table_args__ = (
        Index(
            'uix_inn_kpp', inn, kpp,
            postgresql_where=and_(inn.isnot(None), kpp.isnot(None)),
        ),
    )

    accounts: Mapped[List['BankAccount']] = relationship(backref='bank')
