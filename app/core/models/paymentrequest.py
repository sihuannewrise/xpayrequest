from datetime import datetime
from typing import List, Optional
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base


class PaymentRequest(Base):
    author: Mapped[UUID] = mapped_column(ForeignKey('user.id'))
    type_id: Mapped[int] = mapped_column(ForeignKey('paymenttype.id'))
    payer_id: Mapped[int] = mapped_column(ForeignKey('company.id'))
    recipient_id: Mapped[int] = mapped_column(ForeignKey('counteragent.id'))

    created_on: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_on: Mapped[datetime] = mapped_column(onupdate=func.now())

    kfp_id: Mapped[Optional[int]] = mapped_column(ForeignKey('kfp.id'))
    due_date: Mapped[Optional[datetime]]
    purpose: Mapped[Optional[str]] = mapped_column(String(210))
    amount_netto: Mapped[Optional[float]]
    amount_vat: Mapped[Optional[float]]
    amount_total: Mapped[Optional[float]]
    attach_url: Mapped[Optional[str]] = mapped_column(String(150))

    field_101_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('payerstatus.id'))
    field_104_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('kbk.id'))
    field_105_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('oktmo.id'))
    field_106: Mapped[Optional[str]] = mapped_column(
        String(20))  # Основание платежа
    field_107: Mapped[Optional[str]] = mapped_column(
        String(20))  # Налоговый период
    field_108: Mapped[Optional[str]] = mapped_column(
        String(20))  # Номер документа-основания платежа
    field_109: Mapped[Optional[str]] = mapped_column(
        String(20))  # Дата документа-основания платежа

    project: Mapped[Optional[str]] = mapped_column(String(50))
    contract: Mapped[Optional[str]] = mapped_column(String(50))
    contract_date: Mapped[Optional[datetime]]
    sub_contract: Mapped[Optional[str]] = mapped_column(String(50))
    sub_contract_date: Mapped[Optional[datetime]]
    prepayment_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('prepayment.id'))

    register: Mapped['PaymentRegister'] = relationship(backref='pr')
    proc: Mapped[List['PaymentProcessing']] = relationship(backref='pr')

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} ('
            f'pr_id={self.id}, payer_id={self.payer_id})>'
        )
