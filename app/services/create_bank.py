# command to run this script from root dir:  python -m app.services.create_bank
# creating bank by id (BIC, SWIFT or INN) from dadata

import asyncio
import aiofiles
from datetime import datetime as dt

from contextlib import asynccontextmanager

from app.services.dadata import dadata_find_bank
from app.core.db import get_async_session
from app.core.models.bank import Bank
from app.services.config.biclist import BICS
from app.services.config.mapping import DATE_FIELDS

get_async_session_context = asynccontextmanager(get_async_session)


async def get_bic_list(filename):
    """Формирует из файла множество с БИКами банков.
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


async def check_bic_duplicate(bic: str, session):
    """
    Проверяет наличие БИК в БД перед внесением новой записи.
    """
    bank = await session.get(Bank, bic)
    if bank is not None:
        raise ValueError(
            f'Значение \033[1m{bic}\033[0m уже существует '
            f'в таблице \033[1m{Bank.__name__.lower()}\033[0m !'
        )
    return None


async def get_bank_by_id(id: str):
    """
    Получает из сервиса dadata информацию о банке по его ID (БИК, ИНН, свифт).
    Информацию парсит в словарь по интересующим полям.
    Возвращает словарь или None.
    """
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
            'treasury_accounts': data['data']['treasury_accounts'],
            'opf_type': data['data']['opf']['type'],
        }
        for field in DATE_FIELDS:
            if bank[field] is not None:
                bank[field] = dt.fromtimestamp(bank[field]/1000)
        if isinstance(bank['treasury_accounts'], list):
            bank['treasury_accounts'] = bank['treasury_accounts'][0]
        return bank
    except IndexError:
        print('No DAData')


async def create_bank_by_id(
    bic: str, bank_info: dict, session, is_archived: bool = False,
) -> None:
    """
    Создание в БД записи о новом банке.
    Перед записью сверяет, нет ли в БД существующей записи с БИКом.
    Добавляет в словарь дополнительные ключи.
    """
    try:
        extra_fields = {
            'is_archived': is_archived,
            'description': 'autoloaded from DAData',
        }
        bank_info.update(extra_fields)
        await check_bic_duplicate(bic, session)
        model = Bank()
        for field in bank_info:
            setattr(model, field, bank_info[field])
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return None
    except ValueError:
        print(f'No dadata on {bic}')
        return None


async def create_milti_banks(bics: set):
    async with get_async_session_context() as session:
        for bic in bics:
            dadata = await get_bank_by_id(bic)
            if dadata is not None:
                await create_bank_by_id(bic, dadata, session)
    return None


if __name__ == "__main__":
    # asyncio.run(get_bank_by_id('004525988'))  # УФК
    # asyncio.run(get_bank_by_id('044579132'))

    # asyncio.run(get_bic_list('app/services/config/biclist.txt'))
    asyncio.run(create_milti_banks(BICS))
