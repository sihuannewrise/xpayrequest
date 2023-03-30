from typing import Optional
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models._common import BaseWithPK


class BankAccount(BaseWithPK):
    account: Mapped[str] = mapped_column(String(20))
    currency: Mapped[Optional[str]] = mapped_column(String(20))
    bank_bic: Mapped[Optional[str]] = mapped_column(ForeignKey('bank.bic'))
    ca_id: Mapped[int] = mapped_column(ForeignKey('counteragent.id'),)
    type_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('bankaccounttype.id'))
    is_default: Mapped[Optional[bool]]

    __table_args__ = (UniqueConstraint(
        'account', 'bank_bic', name='_account_bank_unique',
    ),)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.account})>'
