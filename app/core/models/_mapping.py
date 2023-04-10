from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models._common import BaseWithPK


class CaKppMapping(BaseWithPK):
    ca_inn: Mapped[int] = mapped_column(
        ForeignKey('counteragent.inn'), index=True)
    kpp_name: Mapped[int] = mapped_column(ForeignKey('kpp.name'), index=True)
    valid_from: Mapped[Optional[datetime]]
    valid_till: Mapped[Optional[datetime]]

    __table_args__ = (
        UniqueConstraint('ca_inn', 'kpp_name', name='_innkppmapping_unique'),)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.ca_inn}-{self.kpp_name})>'


class ParentChildMapping(BaseWithPK):
    parent_name: Mapped[int] = mapped_column(ForeignKey('counteragent.name'))
    child_name: Mapped[int] = mapped_column(ForeignKey('counteragent.name'))

    __table_args__ = (
        UniqueConstraint(
            'parent_name', 'child_name', name='_parentchild_unique'),
    )

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} (Parent'
            f'{self.parent_name}-Child{self.child_name})>'
        )
