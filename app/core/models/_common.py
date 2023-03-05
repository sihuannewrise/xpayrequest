from datetime import datetime
from typing import Optional
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base
from app.core.models.aux.selectchoice import EntityStatus


class EntityBase(Base):
    __abstract__ = True

    name: Mapped[str] = mapped_column(String(150), unique=True)
    address: Mapped[Optional[str]] = mapped_column(String(200))
    status: Mapped[Optional[EntityStatus]]
    inn: Mapped[Optional[str]] = mapped_column(String(12))
    kpp: Mapped[Optional[str]] = mapped_column(String(9))
    __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)

    actuality_date: Mapped[Optional[datetime]]
    registration_date: Mapped[Optional[datetime]]
    liquidation_date: Mapped[Optional[datetime]]


class SupplementaryBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(50), unique=True)


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


class KFP(SupplementaryBase):
    """
    код финансовой позиции
    """
    payments = relationship('PaymentRequest')


class PayerStatus(SupplementaryBase):
    """
    Статус плательщика
    """
    payments = relationship('PaymentRequest')


class KBK(SupplementaryBase):
    """
    КБК
    """
    payments = relationship('PaymentRequest')


class OKTMO(SupplementaryBase):
    """
    ОКТМО
    """
    payments = relationship('PaymentRequest')


class Prepayment(SupplementaryBase):
    """
    Платеж авансовый или по факту
    """
    payments = relationship('PaymentRequest')


class PaymentStatus(SupplementaryBase):
    """
    статус платежа: у исполнителя, на подписи, на исполнении
    """
    payments = relationship('PaymentRegister')
