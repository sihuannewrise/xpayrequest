# command to run this script from root dir:  python -m app.services.supplementarycreate  # noqa

import asyncio
from contextlib import asynccontextmanager
from sqlalchemy import select

from app.core.db import get_async_session
from app.core.models._common import (
    BankAccountType, PaymentType, KFP, PaymentStatus, KBK, OKTMO, Prepayment,
    PayerStatus, PaymentVerdict, KPP, CounterAgentGroup, Currency,
)
from app.services.config.mapping import SUPPLEMENTARY_SCHEMAS, KPP_LIST

get_async_session_context = asynccontextmanager(get_async_session)

# Don't forget update this dictionary in app.services.config.mapping file
MAPPING = {
    'BankAccountType': BankAccountType,
    'PaymentType': PaymentType,
    'KFP': KFP,
    'PayerStatus': PayerStatus,
    'KBK': KBK,
    'OKTMO': OKTMO,
    'Prepayment': Prepayment,
    'PaymentStatus': PaymentStatus,
    'PaymentVerdict': PaymentVerdict,
    'KPP': KPP,
    'CounterAgentGroup': CounterAgentGroup,
    'Currency': Currency,
}


async def check_name_duplicate(model, name, session):
    obj = await session.scalar(
        select(model).where(model.name == name)
    )
    if obj is not None:
        raise ValueError(
            f'Значение \033[1m{name}\033[0m уже существует '
            f'в таблице \033[1m{model.__name__.lower()}\033[0m !'
        )
    return obj


async def fill_supp_tables():
    async with get_async_session_context() as session:
        for model_str, schema in SUPPLEMENTARY_SCHEMAS.items():
            for name, desc in schema.items():
                try:
                    model = MAPPING[model_str]
                    await check_name_duplicate(model, name, session)
                    db_obj = model(name=name, description=desc)
                    session.add(db_obj)
                except ValueError:
                    print(
                        f'Значение \033[1m{name}\033[0m уже существует '
                        f'в таблице \033[1m{model.__name__.lower()}\033[0m'
                    )
            await session.commit()


async def fill_kpp():
    async with get_async_session_context() as session:
        kpp_list_to_add = []
        for kpp in KPP_LIST:
            kpp_list_to_add.append(KPP(name=kpp))
        session.add_all(kpp_list_to_add)
        await session.commit()
        return None


if __name__ == "__main__":
    # asyncio.run(fill_kpp())
    asyncio.run(fill_supp_tables())
