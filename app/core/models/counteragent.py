from sqlalchemy import Column, DateTime, String

from app.core.db import EntityBase


class CounterAgents(EntityBase):
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
