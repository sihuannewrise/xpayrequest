from sqlalchemy import Column, Integer, String

from app.core.db import EntityBase


class Banks(EntityBase):
    # name = Column(String(150), unique=True, nullable=False)
    bic = Column(Integer, unique=True, nullable=False)
    correspondent_account = Column(String(20))
    payment_city = Column(String(150), nullable=False)
    
    swift = Column(String(11))
    # inn = Column(Integer)
    # kpp = Column(Integer)
    # __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)
    registration_number = Column(Integer)
    treasury_accounts = Column(String(20))
    opf_type = Column(String(50))
    # address = Column(String(200))
    # actuality_date = Column(DateTime)
    # registration_date = Column(DateTime)
    # liquidation_date = Column(DateTime)
    # status = Column(String(20))
