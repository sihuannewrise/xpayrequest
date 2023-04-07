# command to run this script from root dir:  python -m app.services.counteragentcreate  # noqa
# creating ca by id (INN or OGRN) from dadata

import os
import asyncio
import aiofiles
from datetime import datetime as dt
from contextlib import asynccontextmanager

from sqlalchemy import select
from app.services.dadata import dd_find_by_id
from app.core.db import get_async_session
from app.core.models.counteragent import CounterAgent

# from app.services.config.listca import BICS
from app.services.config.mapping import DATE_FIELDS, DD_SEARCH_SUBJECT

get_async_session_context = asynccontextmanager(get_async_session)


async def get_counteragent_list(filename):
    inn_set = set()
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            inn_set.add(line.strip())
        return inn_set


async def stuff_ca_with_data(
    ca_info: dict, is_archived: bool = False,
    description: str = 'autoloaded',
):
    data = ca_info[0]
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


async def add_all_counteragents(inn_list: list) -> None:
    """
    """
    async with get_async_session_context() as session:
        real_counteragents = []
        inns_from_db = await session.scalars(select(CounterAgent.inn))
        inns_from_db = inns_from_db.all()
        raw_bics = set(bics).difference(set(bics_from_db))
        for bic in raw_bics:
            candidate_bank = await dd_find_by_id(
                DD_SEARCH_SUBJECT['counteragent'], bic,
            )
            if not candidate_bank:
                continue
            new_bank = await stuff_bank_with_data(
                candidate_bank, is_archived=False,
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
    # asyncio.run(get_counteragent_list('app/services/config/listca.py'))

    print(asyncio.run(dd_find_by_id('party', '7707441644'))[0])
