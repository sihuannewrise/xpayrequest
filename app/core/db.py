from typing import Optional
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase, declared_attr, Mapped, mapped_column, sessionmaker,
)

from app.core.config import settings
from app.core.models.aux.annotsettings import ans


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[Optional[str]] = mapped_column(String(150))

    created_on: Mapped[ans.timestamp]
    updated_on: Mapped[ans.timestamp_upd]
    is_archived: Mapped[ans.bool_0]


engine = create_async_engine(settings.database_url, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
