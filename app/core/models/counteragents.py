from sqlalchemy import Column, Integer, String, UniqueConstraint

from app.core.db import Base


class CounterAgents(Base):
    name = Column(String(100), nullable=False)
    full_name = Column(String(150))

    inn = Column(Integer, nullable=False)
    kpp = Column(Integer, nullable=False)
    __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)
