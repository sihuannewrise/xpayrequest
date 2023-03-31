from datetime import datetime
from typing import Optional

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.models._common import EntityBase
from app.core.models._selectchoice import CounterAgentType


class CounterAgent(EntityBase):
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, index=True)

    ogrn: Mapped[Optional[str]] = mapped_column(String(20))
    ogrn_date: Mapped[Optional[datetime]]
    ca_type: Mapped[Optional[CounterAgentType]]
    opf_short: Mapped[Optional[str]] = mapped_column(String(10))
    name_short_with_opf: Mapped[Optional[str]] = mapped_column(String(150))
    ip_surname: Mapped[Optional[str]] = mapped_column(String(50))
    ip_name: Mapped[Optional[str]] = mapped_column(String(50))
    ip_patronymic: Mapped[Optional[str]] = mapped_column(String(50))
    management_post: Mapped[Optional[str]] = mapped_column(String(50))
    management_disqualified: Mapped[Optional[str]] = mapped_column(String(50))
    management_name: Mapped[Optional[str]] = mapped_column(String(150))
    address_full: Mapped[Optional[str]] = mapped_column(String(150))

    __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)

    bank_accounts: Mapped['BankAccount'] = relationship(backref='ca')
    payments: Mapped['PaymentRequest'] = relationship(backref='ca')
