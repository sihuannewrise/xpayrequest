from typing import List
from sqlalchemy.orm import relationship, Mapped
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTableUUID,
)

from app.core.db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    employee: Mapped['Employee'] = relationship(backref='user')
    pr_list: Mapped[List['PaymentRequest']] = relationship(backref='user')
    register: Mapped[List['PaymentRegister']] = relationship(backref='user')
    proc: Mapped[List['PaymentProcessing']] = relationship(backref='user')

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.email})>'


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass
