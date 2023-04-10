# command to run this script from root dir:  python -m app.services.bankcreate
# creating bank by id (BIC, SWIFT or INN) from dadata

import os
import asyncio
import aiofiles
from datetime import datetime as dt
from contextlib import asynccontextmanager

from sqlalchemy import select
from app.services.dadata import dd_find_by_id
from app.core.db import get_async_session
from app.core.models.bank import Bank

from app.services.config.listbic import BICS
from app.services.config.mapping import DATE_FIELDS, DD_SEARCH_SUBJECT

get_async_session_context = asynccontextmanager(get_async_session)


async def get_bank_list(filename):
    bic_set = set()
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            bic_set.add(line.strip())
        return bic_set


async def check_no_bic_duplicate(bic: str, session):
    bank = await session.get(Bank, bic)
    if bank is not None:
        raise ValueError(
            f'БИК \033[1m{bic}\033[0m уже в таблице '
            f'\033[1m{Bank.__name__.lower()}\033[0m !'
        )


async def stuff_bank_with_data(
    data: dict, is_archived: bool = False,
    description: str = 'autoloaded',
):
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
    bank = {k: v for k, v in bank.items() if v is not None}
    for field in DATE_FIELDS:
        if field in bank:
            bank[field] = dt.fromtimestamp(bank[field]/1000)
    if 'treasury_accounts' in bank and isinstance(
        bank['treasury_accounts'], list
    ):
        bank['treasury_accounts'] = bank['treasury_accounts'][0]
    extra_fields = {
        'is_archived': is_archived,
        'description': description,
    }
    bank.update(extra_fields)
    return bank


async def add_all_banks(bics: set) -> None:
    """
    Отфильтровывает вх данные, отсеивая те, что уже есть в БД.
    Оставшиеся БИКи обрабатываются дальше.
    Получает из БД список всех БИКов. Создает список моделей с данными
    банков и записывает в БД сразу все банки из списка (метод add_all).
    """
    async with get_async_session_context() as session:
        real_banks = []
        bics_from_db = await session.scalars(select(Bank.bic))
        bics_from_db = bics_from_db.all()
        raw_bics = set(bics).difference(set(bics_from_db))
        for bic in raw_bics:
            candidate_bank = await dd_find_by_id(
                DD_SEARCH_SUBJECT['bank'], bic,
            )
            if not candidate_bank:
                continue
            new_bank = await stuff_bank_with_data(
                candidate_bank[0], is_archived=False,
                description=f'autoloaded from {os.path.basename(__file__)}'
            )
            model = Bank()
            for field in new_bank:
                setattr(model, field, new_bank[field])
            real_banks.append(model)
        if real_banks:
            session.add_all(real_banks)
            await session.commit()
        return None


if __name__ == "__main__":
    # print(asyncio.run(dd_find_bank('007182108')))
    # asyncio.run(get_bank_list('app/services/config/listbic.txt'))

    asyncio.run(add_all_banks(BICS))
