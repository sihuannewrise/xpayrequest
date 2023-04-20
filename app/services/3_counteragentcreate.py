# command to run this script from root dir:  python -m app.services.3_counteragentcreate  # noqa
# creating ca by id (INN or OGRN) from dadata
# httpx.ReadTimeout
# httpx.ConnectTimeout

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
from app.services.config.mapping import (
    DATE_FIELDS, DD_SEARCH_SUBJECT, CA_GROUP_MAPPING,
)

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


def get_kpp_list(ikpp: dict):
    kpp_set = set()
    for _, kpps in ikpp.items():
        if kpps:
            for kpp in kpps:
                kpp_set.add(kpp)
    return kpp_set


async def check_duplicate_by_field(model, field, field_value, session):
    col = getattr(model, field)
    duplicate = await session.scalar(select(col).where(col == field_value))
    if duplicate is not None:
        raise IndexError(
            f'Значение {field}=\033[1m{field_value}\033[0m уже в таблице '
            f'\033[1m{model.__name__.lower()}\033[0m !'
        )


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
    if entity['opf_short'] in CA_GROUP_MAPPING:
        group_name = CA_GROUP_MAPPING[entity['opf_short']]
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
                'management_post': data['data']['management']['post'],
                'management_disqualified':
                    data['data']['management']['disqualified'],
            }
            if management['management_post']:
                management.update({
                    'management_post':
                        management['management_post'].capitalize()
                })
            entity.update(management)
        legal = {
            'branch_type': data['data']['branch_type'],
            'kpp': data['data']['kpp'],
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


async def add_to_counteragent(model, inn, session):
    try:
        await check_duplicate_by_field(model, 'inn', inn, session)
    except IndexError as e:
        print(e)
    else:
        candidate = await dd_find_by_id(
            DD_SEARCH_SUBJECT['counteragent'], inn,
        )
        if not candidate:
            raise ValueError(f'No dadata on \033[1m{inn}\033[0m !')
        new_ca = await stuff_entity_with_data(
            candidate[0],
            is_archived=False,
            description=f'autoloaded by {os.path.basename(__file__)}'
        )
        ca_model = model()
        for field in new_ca:
            setattr(ca_model, field, new_ca[field])
            session.add(ca_model)
        if hasattr(ca_model, 'kpp') and ca_model.kpp:
            return ca_model.kpp
        return None


async def add_to_kpp(model, kpp, session):
    try:
        await check_duplicate_by_field(model, 'name', kpp, session)
    except IndexError as e:
        print(e)
    else:
        kpp_model = model(
            name=kpp,
            description=f'autoloaded by {os.path.basename(__file__)}',
        )
        session.add(kpp_model)
        return None


async def add_all_to_kpp(kpp_set):
    async with get_async_session_context() as session:
        db_kpps = await session.scalars(select(KPP.name))
        db_kpps = db_kpps.all()
        new_kpps = kpp_set.difference(set(db_kpps))
        for kpp in new_kpps:
            kpp_model = KPP(
                name=kpp,
                description=f'autoloaded from {os.path.basename(__file__)}',
            )
            session.add(kpp_model)
        await session.commit()


async def add_to_cakppmapping(
    model, inn_field, inn, kpp_field, kpp, session,
    is_basic: bool = False,
    valid_from: dt = None,
    description: str = f'autoloaded by {os.path.basename(__file__)}',
):
    try:
        inn_col = getattr(model, inn_field)
        kpp_col = getattr(model, kpp_field)
        kpp_list = await session.scalars(
            select(kpp_col).where(inn_col == inn))
        kpp_list = kpp_list.all()
        if kpp in kpp_list:
            raise ValueError(
                f'Запись {inn_field}=\033[1m{inn}\033[0m '
                f'{kpp_field}=\033[1m{kpp}\033[0m уже в таблице '
                f'\033[1m{model.__name__.lower()}\033[0m !'
            )
        mapping_model = model(
            ca_inn=inn,
            kpp_name=kpp,
            is_basic=is_basic,
            valid_from=valid_from,
            description=description,
        )
        session.add(mapping_model)
    except Exception as e:
        print(e)


async def add_multi_records(data: dict) -> None:
    async with get_async_session_context() as session, session.begin():
        for inn, kpps in data.items():
            try:
                dd_kpp = await add_to_counteragent(
                    CounterAgent, inn, session)
                await session.commit()
            except ValueError as e:
                print(e)
            else:
                for kpp in kpps:
                    await add_to_kpp(KPP, kpp, session)
                    try:
                        is_basic = False
                        if kpp == dd_kpp:
                            is_basic = True
                        await add_to_cakppmapping(
                            CaKppMapping, 'ca_inn', inn,
                            'kpp_name', kpp, session,
                            is_basic=is_basic,
                        )
                    except ValueError as e:
                        print(e)
        return None


async def add_one_ca(inn: str) -> None:
    async with get_async_session_context() as session:
        try:
            dd_kpp = await add_to_counteragent(CounterAgent, inn, session)
            await session.commit()
        except ValueError as e:
            print(e)
        else:
            if dd_kpp:
                await add_to_kpp(KPP, dd_kpp, session)
        finally:
            if dd_kpp:
                try:
                    await add_to_cakppmapping(
                        CaKppMapping, 'ca_inn', inn,
                        'kpp_name', dd_kpp, session,
                        is_basic=True,
                    )
                except ValueError as e:
                    print(e)


if __name__ == "__main__":
    # asyncio.run(get_counteragent_list('app/services/config/listca.py'))
    # asyncio.run(add_all_to_kpp(get_kpp_list(IKPP_DICT)))

    # dd_ca = asyncio.run(dd_find_by_id('party', '1102079562'))
    # print(dd_ca)
    # print(asyncio.run(stuff_entity_with_data(dd_ca[0])))

    # asyncio.run(add_one_ca('5919851303'))
    asyncio.run(add_multi_records(IKPP_DICT))
