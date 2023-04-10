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


async def entity_processing(entity):
    pass


async def stuff_ca_with_data(
    data: dict,
    is_archived: bool = False,
    description: str = 'autoloaded',
    group_name: str = None,
    email: str = None,
):
    entity = {
        'ca_type': data['data']['type'],
        'name': data['data']['name']['full'],
        'opf_short': data['data']['opf']['short'],
        'name_full_with_opf': data['data']['name']['full_with_opf'],
        'status': data['data']['state']['status'],
        'inn': data['data']['inn'],
        'ogrn': data['data']['ogrn'],
        'ogrn_date': data['data']['ogrn_date'],
        'actuality_date': data['data']['state']['actuality_date'],
        'registration_date': data['data']['state']['registration_date'],
        'liquidation_date': data['data']['state']['liquidation_date'],
        'address': data['data']['address']['value'],
        'address_full': data['data']['address']['data']['source'],
    }
    if entity['ca_type'] == 'LEGAL':
        if data['data']['management']:
            management = {
                'management_name': data['data']['management']['name'],
                'management_post': data['data']['management']['post'],
                'management_disqualified':
                    data['data']['management']['disqualified'],
            }
            entity.update(management)
        legal = {
            'branch_type': data['data']['branch_type'],
            'kpp_name': data['data']['kpp'],
        }
        entity.update(legal)
    else:
        individual = {
            'fio_name': data['data']['fio']['name'],
            'fio_patronymic': data['data']['fio']['patronymic'],
            'fio_surname': data['data']['fio']['surname'],
        }
        entity.update(individual)

    entity = {k: v for k, v in entity.items() if v is not None}
    for field in DATE_FIELDS:
        if field in entity:
            entity[field] = dt.fromtimestamp(entity[field]/1000)
    extra_fields = {
        'is_archived': is_archived,
        'description': description,
        'group_name': group_name,
        'email': email,
    }
    entity.update(extra_fields)
    print(entity)
    return None


# async def add_all_counteragents(inn_list: list) -> None:
#     """
#     """
#     async with get_async_session_context() as session:
#         real_counteragents = []
#         inns_from_db = await session.scalars(select(CounterAgent.inn))
#         inns_from_db = inns_from_db.all()
#         raw_bics = set(bics).difference(set(bics_from_db))
#         for bic in raw_bics:
#             candidate_bank = await dd_find_by_id(
#                 DD_SEARCH_SUBJECT['counteragent'], bic,
#             )
#             if not candidate_bank:
#                 continue
#             new_bank = await stuff_bank_with_data(
#                 candidate_bank, is_archived=False,
#                 description=f'autoloaded from {os.path.basename(__file__)}'
#             )
#             model = Bank()
#             for field in new_bank:
#                 setattr(model, field, new_bank[field])
#             real_banks.append(model)
#         if real_banks:
#             session.add_all(real_banks)
#             await session.commit()
#         return None


if __name__ == "__main__":
    # print(asyncio.run(dd_find_bank('007182108')))
    # asyncio.run(get_counteragent_list('app/services/config/listca.py'))

    dd_ca = asyncio.run(dd_find_by_id('party', '7706295292'))
    # print(dd_ca)
    asyncio.run(stuff_ca_with_data(dd_ca[0]))
