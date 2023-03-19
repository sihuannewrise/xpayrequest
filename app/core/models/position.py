from datetime import date
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Position(Base):
    name: Mapped[str] = mapped_column(String(300))
    employer_id: Mapped[int] = mapped_column(ForeignKey('company.id'))
    employee_id: Mapped[int] = mapped_column(ForeignKey('employee.id'))
    from_date: Mapped[Optional[date]]
    till_date: Mapped[Optional[date]]
    full_stack: Mapped[Optional[bool]]

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} ('
            f'{self.name}, employer_id={self.employer_id})>')