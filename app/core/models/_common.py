from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base
from ._selectchoice import EntityStatus


class BaseWithPK(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class SupplementaryBase(BaseWithPK):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(50), unique=True)

    def __repr__(self) -> str:
        if self.description:
            return (
                f'<{self.__class__.__name__} ({self.name}-{self.description})>'
            )
        else:
            return f'<{self.__class__.__name__} ({self.name})>'


class EntityBase(Base):
    __abstract__ = True

    address: Mapped[Optional[str]] = mapped_column(String(200))
    status: Mapped[Optional[EntityStatus]] = mapped_column(String(20))

    actuality_date: Mapped[Optional[datetime]]
    registration_date: Mapped[Optional[datetime]]
    liquidation_date: Mapped[Optional[datetime]]

    is_archived: Mapped[Optional[bool]] = mapped_column(
        server_default=text('FALSE'))

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.name})>'


class BankAccountType(SupplementaryBase):
    """
    основной, инвест, спецсчет
    """
    accounts: Mapped[List['CaAccountMapping']] = relationship(
        backref='bankaccounttype',
    )


class PaymentType(SupplementaryBase):
    """
    контрагенту, в бюджет, инвест
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='paymenttype',
    )


class KFP(SupplementaryBase):
    """
    код финансовой позиции
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='kfp',
    )


class PayerStatus(SupplementaryBase):
    """
    Статус плательщика
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='payerstatus',
    )


class KBK(SupplementaryBase):
    """
    КБК
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='kbk',
    )


class OKTMO(SupplementaryBase):
    """
    ОКТМО
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='oktmo',
    )


class Prepayment(SupplementaryBase):
    """
    Платеж авансовый или по факту
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='prepayment',
    )


class PaymentStatus(SupplementaryBase):
    """
    статус платежа: у исполнителя, на подписи, на исполнении
    """
    register: Mapped[List['PaymentRegister']] = relationship(
        backref='paymentstatus',
    )


class PaymentVerdict(SupplementaryBase):
    """
    решение подписанта: согласовано, на доработку, отклонено
    """
    proc: Mapped[List['PaymentProcessing']] = relationship(
        backref='paymentverdict',
    )


class KPP(SupplementaryBase):
    """
    список КПП
    """
    ca_list: Mapped[List['CaKppMapping']] = relationship(
        backref='kpp',
    )


class CounterAgentGroup(SupplementaryBase):
    """
    группа контрагентов (ЛУКОЙЛ, госорганы)
    """
    ca_list: Mapped[List['CounterAgent']] = relationship(
        backref='counteragentgroup',
    )


class Currency(SupplementaryBase):
    """
    справочник валют
    """
    acc_list: Mapped[List['BankAccount']] = relationship(
        backref='currency',
    )
