from datetime import datetime
from typing import AsyncGenerator, Optional
from sqlalchemy import String, text
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine)
from sqlalchemy.orm import (
    DeclarativeBase, declared_attr, Mapped, mapped_column,
)

from app.core.config import settings


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[Optional[str]] = mapped_column(String(150))

    created_on: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.CURRENT_TIMESTAMP(),
    )
    updated_on: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )


engine = create_async_engine(settings.database_url, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as async_session:
        yield async_session
