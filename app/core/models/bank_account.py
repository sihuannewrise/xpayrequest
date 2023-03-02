from sqlalchemy import (
    Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
)

from app.core.db import Base


class BankAccount(Base):
    account = Column(String(20), nullable=False)
    is_default = Column(Boolean, default=False)
    bank_id = Column(Integer, ForeignKey('bank.id'))
    ca_id = Column(Integer, ForeignKey('counteragent.id'),)
    __table_args__ = (UniqueConstraint(
        'account', 'bank_id', name='_account_bank_unique',
    ),)
