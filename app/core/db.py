from typing import AsyncGenerator, Optional
from sqlalchemy import String
from sqlalchemy.orm import class_mapper
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

    @classmethod
    def _get_keys(cls):
        return class_mapper(cls).c.keys()

    def get_dict(self):
        d = {}
        for k in self._get_keys():
            d[k] = getattr(self, k)
        return d


engine = create_async_engine(
    settings.database_url,
    # connect_args={"ssl": {"key": settings.sqlalchemy_database_pem}},
    # echo=True,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as async_session:
        yield async_session
