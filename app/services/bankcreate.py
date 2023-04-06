# command to run this script from root dir:  python -m app.services.bankcreate
# creating bank by id (BIC, SWIFT or INN) from dadata

import asyncio
import aiofiles
from datetime import datetime as dt
from contextlib import asynccontextmanager

from sqlalchemy import select
from app.services.dadata import dd_find_bank
from app.core.db import get_async_session
from app.core.models.bank import Bank

from app.services.config.biclist import BICS
from app.services.config.mapping import DATE_FIELDS

get_async_session_context = asynccontextmanager(get_async_session)


async def get_bic_list(filename):
    """Формирует из файла множество с БИКами.
    Args:
        filename (txt): столбец с кодами
    Returns:
        set: перечень БИК
    """
    bic_set = set()
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            bic_set.add(line.strip())
        return bic_set


async def check_no_bic_duplicate(bic: str, session):
    """
    Проверяет наличие БИК в БД перед внесением новой записи.
    Args:
        bic (str): БИК
    Returns:
        None или ошибку, если проверка не пройдена, т.е. есть дубликат в БД.
    """
    bank = await session.get(Bank, bic)
    if bank is not None:
        raise ValueError(
            f'БИК \033[1m{bic}\033[0m уже в таблице '
            f'\033[1m{Bank.__name__.lower()}\033[0m !'
        )


async def dd_get_bank_by_id(id: str):
    """
    Получает из сервиса dadata информацию о банке по его ID (БИК, ИНН, свифт).
    Args:
        id (str): БИК
    Returns:
        словарь с данными банка или ошибку.
    Информацию парсит в словарь по интересующим полям.
    Удаляет поля со значением None, форматирует поля с датами в datetime,
    из поля "казначейские счета" (treasury_accounts) берет из списка
    первое значение.
    """
    data = await dd_find_bank(id)
    if not data:
        raise IndexError(f'DaData: нет данных по \033[1m{id}\033[0m')
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
    return bank


async def stuff_bank_with_data(
    bank_info: dict, is_archived: bool = False,
):
    data = bank_info[0]
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
        'description': 'autoloaded from DAData',
    }
    bank.update(extra_fields)
    return bank


async def bank_create(
    bic: str, bank_info: dict, session, is_archived: bool = False,
):
    """
    Создание в БД записи о новом банке.
    Args:
        bic (str) - БИК, bank_info (dict) - словарь с данными по банку
    Returns:
        Данные банка, записанные в БД.

    Данные должны поступать корректные (не None, например).
    Перед записью сверяет, нет ли в БД существующей записи с БИКом.
    Добавляет в словарь дополнительные ключи is_archived и description.
    """
    try:
        await check_no_bic_duplicate(bic, session)
        extra_fields = {
            'is_archived': is_archived,
            'description': 'autoloaded from DAData',
        }
        bank_info.update(extra_fields)
        model = Bank()
        for field in bank_info:
            setattr(model, field, bank_info[field])
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return model
    except Exception as e:
        print(e)


async def add_banks(bics: set) -> None:
    """
    Записывает в БД по одной модели из списка БИКов (метод add).
    """
    async with get_async_session_context() as session:
        for bic in bics:
            try:
                dadata = await dd_get_bank_by_id(bic)
                await bank_create(bic, dadata, session)
            except Exception as e:
                print(e)


async def add_all_banks(bics: set) -> None:
    """
    Получает из БД список всех БИКов. Отфильтровывает вх данные, отсеивая те,
    что уже есть в БД. Оставшиеся БИКи обрабатываются дальше.
    Создает список моделей с данными банков и записывает в БД сразу
    все банки из списка (метод add_all).
    """
    async with get_async_session_context() as session:
        real_banks = []
        bics_from_db = await session.scalars(select(Bank.bic))
        bics_from_db = bics_from_db.all()
        raw_bics = set(bics).difference(set(bics_from_db))
        for bic in raw_bics:
            candidate_bank = await dd_find_bank(bic)
            if not candidate_bank:
                continue
            new_bank = await stuff_bank_with_data(
                candidate_bank, is_archived=False,
            )
            model = Bank()
            for field in new_bank:
                setattr(model, field, new_bank[field])
            real_banks.append(model)
        session.add_all(real_banks)
        await session.commit()
        return None


if __name__ == "__main__":
    # asyncio.run(get_bank_by_id('004525988'))  # УФК
    # print(asyncio.run(get_bank_by_id('007182108')))

    # asyncio.run(get_bic_list('app/services/config/biclist.txt'))

    asyncio.run(add_all_banks(BICS))
