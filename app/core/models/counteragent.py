from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base
from app.core.models._common import EntityBase
from app.core.models.aux.selectchoice import CounterAgentType


class CounterAgent(EntityBase):
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
    address_full_with_index: Mapped[Optional[str]] = mapped_column(String(150))
    address_egrul: Mapped[Optional[str]] = mapped_column(String(150))
    bank_accounts = relationship('BankAccount')
    payments = relationship('PaymentRequest')


class Payer(Base):
    id: Mapped[int] = mapped_column(
        ForeignKey('counteragent.id'), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
