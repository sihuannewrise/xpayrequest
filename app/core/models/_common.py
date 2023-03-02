from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint

from app.core.db import Base


class EntityBase(Base):
    __abstract__ = True

    name = Column(String(150), unique=True, nullable=False)
    inn = Column(Integer)
    kpp = Column(Integer)
    __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)
    address = Column(String(200))

    actuality_date = Column(DateTime)
    registration_date = Column(DateTime)
    liquidation_date = Column(DateTime)
    status = Column(String(20))
