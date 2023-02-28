from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint

from app.core.db import Base
from app.core.models.bank import Banks
from app.core.models.counteragent import CounterAgents


class BankAccounts(Base):
    account = Column(String(20), nullable=False)
    bank_id = Column(Integer, ForeignKey(Banks.id))
    ca_id = Column(
        Integer,
        ForeignKey(
            CounterAgents.id,
            ondelete='CASCADE',
        ),
        unique=True,
        nullable=False,
    )
    __table_args__ = (UniqueConstraint(
        'account', 'bank_id', name='_account_bank_unique',
    ),)
