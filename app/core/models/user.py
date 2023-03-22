from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTableUUID,
)

from app.core.db import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.email})>'


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.token})>'
