from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.orm import relationship

from app.core.models._common import EntityBase


class CounterAgent(EntityBase):
    on_behalf = Column(Boolean, default=False)  # we can act on CA behalf
    ogrn = Column(String(20))
    ogrn_date = Column(DateTime)
    counteragent_type = Column(String(50))
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
