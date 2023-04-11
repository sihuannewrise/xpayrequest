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
from app.core.models import CaKppMapping, CounterAgent, KPP

from app.services.config.listca import IKPP_DICT
from app.services.config.mapping import DATE_FIELDS, DD_SEARCH_SUBJECT

get_async_session_context = asynccontextmanager(get_async_session)


async def get_counteragent_list(filename):
    ikpp_dict = dict()
    kpp_set = set()
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            inn, *kpp = line.split()
            kpp_set.update(kpp)
            if inn in ikpp_dict:
                ikpp_dict[inn].update(kpp)
            else:
                ikpp_dict.update({inn: set(kpp)})
        return ikpp_dict


async def check_name_duplicate(model, name: str):
    async with get_async_session_context() as session:
        record = await session.scalar(
            select(model.name).where(model.name == name)
        )
        await session.close()
        if record is not None:
            raise ValueError(
                f'Запись \033[1m{name}\033[0m уже в таблице '
                f'\033[1m{model.__name__.lower()}\033[0m !'
            )


async def add_record_to_table(model, record):
    async with get_async_session_context() as session:
        db_table = model(name=record)
        session.add(db_table)
        session.commit
        # await session.refresh(db_table)
        print(db_table)
        return None


async def stuff_entity_with_data(
    data: dict,
    is_archived: bool = False,
    description: str = 'autoloaded',
    group_name: str = None,
    email: str = None,
) -> dict:
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
    extra_fields = {
        'is_archived': is_archived,
        'description': description,
        'group_name': group_name,
        'email': email,
    }
    entity.update(extra_fields)
    if entity['ca_type'] == 'LEGAL':
        if data['data']['management']:
            management = {
                'management_name': data['data']['management']['name'],
                'management_post':
                    data['data']['management']['post'],
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

    return entity


async def add_counteragent(data: dict) -> None:
    """
    """
    async with get_async_session_context() as session:
        for inn, kpps in data.items():
            print(inn)
            for kpp in kpps:
                try:
                    await check_name_duplicate(KPP, kpp)
                    await add_record_to_table(KPP, kpp)
                except Exception as e:
                    print(e)
            # candidate = await dd_find_by_id(
            #     DD_SEARCH_SUBJECT['counteragent'], inn,
            # )
            # if not candidate:
            #     continue
            # new_ca = await stuff_entity_with_data(
            #     candidate, is_archived=False,
            #     description=f'autoloaded from {os.path.basename(__file__)}'
            # )
            # ca_model = CounterAgent()
            # for field in new_ca:
            #     setattr(ca_model, field, new_ca[field])
        # if real_counteragents:
        #     session.add_all(real_counteragents)
        #     await session.commit()
            # await session.refresh(db_obj)
        return None


if __name__ == "__main__":
    # print(asyncio.run(dd_find_record('007182108')))
    # asyncio.run(get_counteragent_list('app/services/config/listca.py'))

    # dd_ca = asyncio.run(dd_find_by_id('party', '9909249880'))
    # print(dd_ca)
    # print(asyncio.run(stuff_entity_with_data(dd_ca[0])))
    asyncio.run(add_counteragent(IKPP_DICT))
