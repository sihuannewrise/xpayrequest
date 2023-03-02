from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import EntityBase


class Bank(EntityBase):
    bic = Column(Integer, unique=True, nullable=False)
    correspondent_account = Column(String(20))
    payment_city = Column(String(50), nullable=False)

    swift = Column(String(11))
    registration_number = Column(Integer)
    treasury_accounts = Column(String(20))
    opf_type = Column(String(50))

    accounts = relationship('BankAccount', cascade='delete')
