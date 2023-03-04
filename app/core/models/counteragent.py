from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base
from app.core.models._common import EntityBase
from app.core.models.aux.selectchoice import CounterAgentType


class CounterAgent(EntityBase):
    on_behalf = Column(Boolean, default=False)  # we can act on CA behalf
    ogrn = Column(String(20))
    ogrn_date = Column(DateTime)
    ca_type: Mapped[CounterAgentType] = mapped_column(nullable=True)
    opf_short = Column(String(10))
    name_short_with_opf = Column(String(150))
    ip_surname = Column(String(100))
    ip_name = Column(String(100))
    ip_patronymic = Column(String(100))
    management_name = Column(String(300))
    management_post = Column(String(100))
    address_full_with_index = Column(String(300))
    address_egrul = Column(String(300))
    bank_accounts = relationship('BankAccount', cascade='delete')
    payments = relationship('PaymentRequest', cascade='delete')


class Payer(Base):
    name = Column(String, unique=True, nullable=False)
    ca_id = Column(Integer, ForeignKey('counteragent.id'), unique=True, nullable=False)
