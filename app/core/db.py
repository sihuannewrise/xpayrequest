from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_archived = Column(Boolean)
    comment = Column(String(100))


Base = declarative_base(cls=PreBase)
engine = create_async_engine(settings.database_url, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
