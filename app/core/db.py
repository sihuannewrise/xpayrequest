from datetime import datetime
from typing_extensions import Annotated
from sqlalchemy import func, String

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase, declared_attr, Mapped, mapped_column, sessionmaker,
)

from app.core.config import settings
# from app.core.models.aux import annotsettings as ans
intpk = Annotated[int, mapped_column(primary_key=True)]
timestamp = Annotated[
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]
str_50 = Annotated[str, mapped_column(String(50), nullable=False)]


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[intpk]
    created_on: Mapped[timestamp]
    updated_on: Mapped[timestamp] = mapped_column(
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_archived: Mapped[bool]
    comment: Mapped[str_50] = mapped_column(nullable=True)


engine = create_async_engine(settings.database_url, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
