# creating bank by BIC, SWIFT or INN from dadata
# command to run this script from root dir:  python -m app.services.create_bank

import asyncio
from dadata import DadataAsync

from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.db import get_async_session
from app.core.user import get_user_db, get_user_manager

get_async_session_context = asynccontextmanager(get_async_session)
get_user_db_context = asynccontextmanager(get_user_db)
get_user_manager_context = asynccontextmanager(get_user_manager)


async def dadata_find_bank(id: str):
    async with DadataAsync(
        settings.dadata_token, settings.dadata_secret,
    ) as dadata:
        result = await dadata.find_by_id(name='bank', query=id)
        return result[0]


async def dadata_suggest_bank(name: str):
    async with DadataAsync(
        settings.dadata_token, settings.dadata_secret,
    ) as dadata:
        result = await dadata.suggest(name='bank', query=name)
        return result


if __name__ == "__main__":
    def get_bank_by_id(id: str):
        data = asyncio.run(dadata_find_bank(id))

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
            'treasury_accounts': data['data']['treasury_accounts'],
            'opf_type': data['data']['opf']['type'],
        }

        for key, value in bank.items():
            print(f'{key} - {value}')
        return None

    # get_bank_by_id('044525985')

    def suggest_bank_names(phrase: str):
        data = asyncio.run(dadata_suggest_bank(phrase))
        for i in range(len(data)):
            print(data[i]['value'])
        return None
