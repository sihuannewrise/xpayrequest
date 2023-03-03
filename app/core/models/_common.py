from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

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


class SupplementaryBase(Base):
    __abstract__ = True
    name = Column(String(50), nullable=False)


class BankAccountType(SupplementaryBase):
    """
    основной, инвест, спецсчет
    """
    accounts = relationship('BankAccount')


class PaymentType(SupplementaryBase):
    """
    контрагенту, в бюджет, инвест
    """
    payments = relationship('PaymentRequest')


class KFP(PaymentType):
    """
    код финансовой позиции
    """
    buh_account = Column(String(20), nullable=False)


class PayerStatus(PaymentType):
    """
    Статус плательщика
    """
    description = Column(String(50))


class KBK(PaymentType):
    """
    КБК
    """
    description = Column(String(150))


class OKTMO(PaymentType):
    """
    ОКТМО
    """
    description = Column(String(150))
