from datetime import date
from typing import Optional, List
from uuid import UUID

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models._common import BaseWithPK


class Employee(BaseWithPK):
    full_name: Mapped[str] = mapped_column(String(300))
    birthdate: Mapped[Optional[date]]

    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    patronymic_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    user_id: Mapped[Optional[UUID]] = mapped_column(ForeignKey('user.id'))

    positions: Mapped[List['Position']] = relationship(backref='employee')

    __table_args__ = (
        UniqueConstraint('full_name', 'birthdate', name='_name_birth_unique'),)

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} ('
            f'{self.full_name}), birthdate={self.birthdate}>')
