from typing import Optional
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models._common import BaseWithPK


class BankAccount(BaseWithPK):
    account: Mapped[str] = mapped_column(String(20), unique=True)
    bank_bic: Mapped[Optional[str]] = mapped_column(ForeignKey('bank.bic'))
    is_default: Mapped[Optional[bool]]
    currency: Mapped[Optional[int]] = mapped_column(ForeignKey('currency.id'))
    type_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('bankaccounttype.id'))

    __table_args__ = (UniqueConstraint(
        'account', 'bank_bic', name='_account_bic_unique',
    ),)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.account})>'
