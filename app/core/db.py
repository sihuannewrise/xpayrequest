from sqlalchemy import text
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

    id: Mapped[ans.intpk]
    created_on: Mapped[ans.timestamp]
    updated_on: Mapped[ans.timestamp] = mapped_column(
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_archived: Mapped[bool]
    comment: Mapped[ans.str_50] = mapped_column(nullable=True)


engine = create_async_engine(settings.database_url, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
