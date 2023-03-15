from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTableUUID,
)

from app.core.db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    patronymic_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))

    pr_list: Mapped[List['PaymentRequest']] = relationship(backref='user')
    register: Mapped[List['PaymentRegister']] = relationship(backref='user')
    proc: Mapped[List['PaymentProcessing']] = relationship(
        backref='user')

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} <{self.email}>'


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass
