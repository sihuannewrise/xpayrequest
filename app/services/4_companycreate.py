# command to run this script from root dir:  python -m app.services.4_companycreate   # noqa

import os
import asyncio
from contextlib import asynccontextmanager
from sqlalchemy import select

from app.core.db import get_async_session
from app.core.models import Company, CounterAgent
from app.services.config.mapping import COMPANIES

get_async_session_context = asynccontextmanager(get_async_session)


async def check_name_duplicate(model, name, session):
    obj = await session.scalar(
        select(model.name).where(model.name == name)
    )
    if obj is not None:
        raise ValueError(
            f'Значение \033[1m{name}\033[0m уже существует '
            f'в таблице \033[1m{model.__name__.lower()}\033[0m !'
        )
    return obj


async def create_companies(description: str = None):
    async with get_async_session_context() as session:
        for inn, name in COMPANIES.items():
            try:
                await check_name_duplicate(Company, name, session)
            except ValueError as e:
                print(e)
            else:
                company = Company(
                    id=await session.scalar(select(
                        CounterAgent.id).where(CounterAgent.inn == inn)),
                    name=name,
                    description=description,
                )
                session.add(company)
        await session.commit()
    return None


if __name__ == "__main__":
    asyncio.run(create_companies(
        description=f'autoloaded by {os.path.basename(__file__)}'))
