from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Payer(Base):
    id: Mapped[int] = mapped_column(
        ForeignKey('counteragent.id'), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.name})>'
