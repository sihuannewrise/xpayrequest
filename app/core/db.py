from typing import AsyncGenerator, Optional
from sqlalchemy import String
from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine)
from sqlalchemy.orm import (
    DeclarativeBase, declared_attr, Mapped, mapped_column,
)

from app.core.config import settings


class Base(DeclarativeBase):
    description: Mapped[Optional[str]] = mapped_column(String(150))

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


engine = create_async_engine(
    settings.database_url,
    # connect_args={"ssl": {"key": settings.sqlalchemy_database_pem}},
    # echo=True,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as async_session:
        yield async_session
