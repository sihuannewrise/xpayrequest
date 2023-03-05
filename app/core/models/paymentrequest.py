from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base


class PaymentRequest(Base):
    type_id: Mapped[int] = mapped_column(ForeignKey('paymenttype.id'))
    payer_id: Mapped[int] = mapped_column(ForeignKey('payer.id'))
    recipient_id: Mapped[int] = mapped_column(ForeignKey('counteragent.id'))

    kfp_id: Mapped[Optional[int]] = mapped_column(ForeignKey('kfp.id'))
    due_date: Mapped[datetime]
    purpose: Mapped[str] = mapped_column(String(210))
    amount_netto: Mapped[Optional[float]]
    amount_vat: Mapped[Optional[float]]
    amount_total: Mapped[float]
    attachement: Mapped[Optional[str]]  = mapped_column(String(150))

    field_101_id: Mapped[Optional[int]] = mapped_column(ForeignKey('payerstatus.id'))
    field_104_id: Mapped[Optional[int]] = mapped_column(ForeignKey('kbk.id'))
    field_105_id: Mapped[Optional[int]] = mapped_column(ForeignKey('oktmo.id'))
    field_106: Mapped[Optional[str]]  = mapped_column(String(20))  # Основание платежа
    field_107: Mapped[Optional[str]]  = mapped_column(String(20))  # Налоговый период
    field_108: Mapped[Optional[str]]  = mapped_column(String(20))  # Номер документа-основания платежа
    field_109: Mapped[Optional[str]]  = mapped_column(String(20))  # Дата документа-основания платежа

    project: Mapped[Optional[str]]  = mapped_column(String(50))
    contract: Mapped[Optional[str]]  = mapped_column(String(50))
    contract_date: Mapped[Optional[datetime]]
    sub_contract: Mapped[Optional[str]]  = mapped_column(String(50))
    sub_contract_date: Mapped[Optional[datetime]]
    prepayment_id: Mapped[int] = mapped_column(ForeignKey('prepayment.id'))

    register: Mapped['PaymentRegister'] = relationship(back_populates='payment_requests')
