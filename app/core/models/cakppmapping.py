from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.models._common import BaseWithPK


class CaKppMapping(BaseWithPK):
    ca_inn: Mapped[int] = mapped_column(ForeignKey('counteragent.inn'),)
    kpp_id: Mapped[int] = mapped_column(ForeignKey('kpp.id'),)
    valid_from: Mapped[Optional[datetime]]
    valid_till: Mapped[Optional[datetime]]

    __table_args__ = (
        UniqueConstraint('ca_inn', 'kpp_id', name='_ca_id_kpp_id_unique'),)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.ca_inn}-{self.kpp_id})>'
