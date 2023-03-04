from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped

from app.core.models._common import EntityBase
from app.core.models.aux.selectchoice import BankOPFType


class Bank(EntityBase):
    bic = Column(Integer, unique=True, nullable=False)
    correspondent_account = Column(String(20))
    payment_city = Column(String(50), nullable=False)

    swift = Column(String(11))
    registration_number = Column(Integer)
    treasury_account = Column(String(20))
    opf_type: Mapped[BankOPFType]

    accounts = relationship('BankAccount')
