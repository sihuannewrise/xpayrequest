from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint

from app.core.db import PreEntityBase


class CounterAgents(PreEntityBase):
    # name = Column(String(100), unique=True, nullable=False)

    # inn = Column(Integer, nullable=False)
    # kpp = Column(Integer, nullable=False)
    # __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)
    ogrn = Column(String(20))
    ogrn_date = Column(DateTime)
    counteragent_type = Column(String(50))
    opf_short = Column(String(10))
    # name_full_without_opf = Column(String(200))
    name_short_with_opf = Column(String(150))
    ip_surname = Column(String(100))
    ip_name = Column(String(100))
    ip_patronymic = Column(String(100))
    management_name = Column(String(300))
    management_post = Column(String(100))
    address_full_with_index = Column(String(300))
    address_egrul = Column(String(300))
    # address = Column(String(200))
    # actuality_date = Column(DateTime)
    # registration_date = Column(DateTime)
    # liquidation_date = Column(DateTime)
    # status = Column(String(20))
