from datetime import datetime
from typing import Optional
from sqlalchemy import String, text
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase, declared_attr, Mapped, mapped_column, sessionmaker,
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
    is_archived: Mapped[bool] = mapped_column(
        default=False,
        server_default=text('FALSE'))


engine = create_async_engine(settings.database_url, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
