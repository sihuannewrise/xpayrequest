from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class PreEntityBase(PreBase):
    name = Column(String(150), unique=True, nullable=False)
    inn = Column(Integer)
    kpp = Column(Integer)
    __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)
    address = Column(String(200))

    actuality_date = Column(DateTime)
    registration_date = Column(DateTime)
    liquidation_date = Column(DateTime)
    status = Column(String(20))


Base = declarative_base(cls=PreBase)

EntityBase = declarative_base(cls=PreEntityBase)

engine = create_async_engine(settings.database_url, echo=True)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
