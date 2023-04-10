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


async def legal_entity_proceccing(entity):
    pass


async def stuff_ca_with_data(
    data: dict,
    is_archived: bool = False,
    description: str = 'autoloaded',
    group_name: str = None,
    email: str = None,
):
    class Entity:
        def __init__(self) -> None:
            self.name = data['data']['name']['full']
            self.opf_short = data['data']['opf']['short']
            self.name_full_with_opf = data['data']['name']['full_with_opf']

            self.status = data['data']['state']['status']
            self.inn = data['data']['inn']
            self.ogrn = data['data']['ogrn']
            self.ogrn_date = data['data']['ogrn_date']
            self.actuality_date = data['data']['state']['actuality_date']
            self.registration_date = data['data']['state']['registration_date']
            self.liquidation_date = data['data']['state']['liquidation_date']

            self.address = data['data']['address']['value']
            self.address_full = data['data']['address']['data']['source']

        def __repr__(self) -> str:
            return f'<{self.__class__.__name__} {self.__dict__}>'

    class Legal(Entity):
        def __init__(self) -> None:
            super().__init__()
            self.branch_type = data['data']['branch_type']
            self.kpp_name = data['data']['kpp']
            self.management = data['data']['management']

    class Individual(Entity):
        def __init__(self) -> None:
            super().__init__()
            self.fio_name = data['data']['fio']['name']
            self.fio_patronymic = data['data']['fio']['patronymic']
            self.fio_surname = data['data']['fio']['surname']

    ca_type = data['data']['type']
    if ca_type == 'LEGAL':
        ca = Legal()
        if ca.management:
            management = {
                'management_name': data['data']['management']['name'],
                'management_post': data['data']['management']['post'],
                'management_disqualified':
                    data['data']['management']['disqualified'],
            }
            for key, value in management.items():
                setattr(ca, key, value)
            print(ca)
    else:
        ca = Individual()

    # ca = {k: v for k, v in ca.items() if v is not None}
    # for field in DATE_FIELDS:
    #     if field in ca:
    #         ca[field] = dt.fromtimestamp(ca[field]/1000)
    # if 'treasury_accounts' in ca and isinstance(
    #     ca['treasury_accounts'], list
    # ):
    #     ca['treasury_accounts'] = ca['treasury_accounts'][0]
    # extra_fields = {
    #     'is_archived': is_archived,
    #     'description': description,
    #     'group_name': group_name,
    #     'email': email,
    # }
    # ca.update(extra_fields)
    # return ca


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
