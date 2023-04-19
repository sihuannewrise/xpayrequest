from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models._common import BaseWithPK


class CaKppMapping(BaseWithPK):
    ca_inn: Mapped[int] = mapped_column(ForeignKey('counteragent.inn'))
    kpp_name: Mapped[int] = mapped_column(ForeignKey('kpp.name'))
    valid_from: Mapped[Optional[datetime]]
    valid_till: Mapped[Optional[datetime]]

    __table_args__ = (
        UniqueConstraint('ca_inn', 'kpp_name', name='uix_inn_kpp_mapping'),)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.ca_inn}-{self.kpp_name})>'


class ParentChildMapping(BaseWithPK):
    parent_name: Mapped[int] = mapped_column(ForeignKey('counteragent.name'))
    child_name: Mapped[int] = mapped_column(ForeignKey('counteragent.name'))

    __table_args__ = (
        UniqueConstraint(
            'parent_name', 'child_name', name='uix_parent_child'),
    )

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} (Parent'
            f'{self.parent_name}-Child{self.child_name})>'
        )


class CaAccountMapping(BaseWithPK):
    ca_inn: Mapped[int] = mapped_column(ForeignKey('counteragent.inn'))
    ca_account: Mapped[int] = mapped_column(ForeignKey('bankaccount.account'))
    type_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('bankaccounttype.id'))
    valid_from: Mapped[Optional[datetime]]
    valid_till: Mapped[Optional[datetime]]
    is_default: Mapped[Optional[bool]]

    __table_args__ = (
        UniqueConstraint(
            'ca_inn', 'ca_account', name='uix_ca_account_mapping'),
    )

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.ca_inn}-{self.ca_account})>'
