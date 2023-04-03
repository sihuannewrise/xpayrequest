# command to run this script from root dir:  python -m app.services.create_bank
# creating bank by BIC, SWIFT or INN from dadata

import asyncio
import aiofiles

from dadata import DadataAsync

from contextlib import asynccontextmanager
from fastapi.encoders import jsonable_encoder

from app.core.config import settings
from app.core.db import get_async_session
from app.core.models.bank import Bank
from app.services.config.biclist import BICS

get_async_session_context = asynccontextmanager(get_async_session)


async def dadata_find_bank(id: str):
    async with DadataAsync(
        settings.dadata_token, settings.dadata_secret,
    ) as dadata:
        result = await dadata.find_by_id(name='bank', query=id)
        return result


async def dadata_suggest_bank(name: str):
    async with DadataAsync(
        settings.dadata_token, settings.dadata_secret,
    ) as dadata:
        result = await dadata.suggest(name='bank', query=name)
        return result


async def check_bic_duplicate(bic: str, session):
    bank = await session.get(Bank, bic)
    if bank is not None:
        raise ValueError(
            f'Значение \033[1m{bic}\033[0m уже существует '
            f'в таблице \033[1m{Bank.__name__.lower()}\033[0m !'
        )
    return None


async def get_bank_by_id(id: str):
    try:
        data = await dadata_find_bank(id)
        data = data[0]
        bank = {
            'name': data['value'],
            'bic': data['data']['bic'],
            'address': data['data']['address']['value'],
            'status': data['data']['state']['status'],
            'inn': data['data']['inn'],
            'kpp': data['data']['kpp'],
            'actuality_date': data['data']['state']['actuality_date'],
            'registration_date': data['data']['state']['registration_date'],
            'liquidation_date': data['data']['state']['liquidation_date'],
            'correspondent_account': data['data']['correspondent_account'],
            'payment_city': data['data']['payment_city'],
            'swift': data['data']['swift'],
            'registration_number': data['data']['registration_number'],
            'treasury_accounts': data['data']['treasury_accounts'][0],
            'opf_type': data['data']['opf']['type'],
        }
        return bank
    except IndexError:
        print('No data')


async def suggest_bank_names(phrase: str):
    data = asyncio.run(dadata_suggest_bank(phrase))
    for i in range(len(data)):
        print(data[i]['value'])
    return None


async def get_bic_list(filename):
    bic_list = set()
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            bic_list.add(line.strip())
        return bic_list


async def create_bank():
    async with get_async_session_context() as session:
        for bic in BICS:
            # await check_bic_duplicate(bic, session)
            bank = Bank()
            dadata = await get_bank_by_id(bic)
            db_obj = jsonable_encoder(dadata)
            for field in db_obj:
                setattr(bank, field, db_obj[field])
            session.add(bank)
            await session.commit()
            await session.refresh(bank)
            print(bank)
            return bank


if __name__ == "__main__":
    # asyncio.run(get_bic_list('app/services/config/biclist.txt'))
    # asyncio.run(get_bank_by_id('007182108'))
    asyncio.run(create_bank())
