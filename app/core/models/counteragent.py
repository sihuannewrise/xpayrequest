from datetime import datetime
from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.models._common import EntityBase
from app.core.models._selectchoice import CounterAgentType, CounterAgentSubsidiary


class CounterAgent(EntityBase):
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, index=True)

    name: Mapped[str] = mapped_column(String(160), unique=True)
    name_short_with_opf: Mapped[Optional[str]] = mapped_column(String(150))
    opf_short: Mapped[Optional[str]] = mapped_column(String(10))

    ca_type: Mapped[Optional[CounterAgentType]]
    group_name: Mapped[str] = mapped_column(
        ForeignKey('CounterAgentGroup.name'), index=True)
    subsidiary: Mapped[Optional[CounterAgentSubsidiary]]

    ogrn: Mapped[Optional[str]] = mapped_column(String(20))
    ogrn_date: Mapped[Optional[datetime]]
    ip_surname: Mapped[Optional[str]] = mapped_column(String(50))
    ip_name: Mapped[Optional[str]] = mapped_column(String(50))
    ip_patronymic: Mapped[Optional[str]] = mapped_column(String(50))
    management_post: Mapped[Optional[str]] = mapped_column(String(50))
    management_disqualified: Mapped[Optional[str]] = mapped_column(String(50))
    management_name: Mapped[Optional[str]] = mapped_column(String(150))
    address_full: Mapped[Optional[str]] = mapped_column(String(150))

    bank_accounts: Mapped[List['BankAccount']] = relationship(backref='ca')
    payments: Mapped[List['PaymentRequest']] = relationship(backref='ca')
    kpp_list: Mapped[List['CaKppMapping']] = relationship(backref='ca')
