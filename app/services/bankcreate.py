# command to run this script from root dir:  python -m app.services.bankcreate
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
    Возвращает True - если проверка пройдена, т.е. нет дубликата в БД,
    и ошибку - если есть.
    """
    bank = await session.get(Bank, bic)
    if bank is not None:
        raise ValueError(
            f'Значение \033[1m{bic}\033[0m уже существует '
            f'в таблице \033[1m{Bank.__name__.lower()}\033[0m !'
        )
    # except HTTPException:
    #         raise HTTPException(
    #             status_code=HTTPStatus.CONFLICT,
    #             detail=f'Значение \033[1m{bic}\033[0m уже существует '
    #                 f'в таблице \033[1m{Bank.__name__.lower()}\033[0m !'
    #         )


async def get_bank_by_id(id: str):
    """
    Получает из сервиса dadata информацию о банке по его ID (БИК, ИНН, свифт).
    Информацию парсит в словарь по интересующим полям.
    Удаляет поля со значением None. Форматирует поля с датами в datetime
    формат и из поля "казначейские счета" (treasury_accounts) берет из списка
    первое значение.
    Возвращает словарь или ошибку.
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
        bank = {k: v for k, v in bank.items() if v is not None}
        for field in DATE_FIELDS:
            if field in bank:
                bank[field] = dt.fromtimestamp(bank[field]/1000)
        if 'treasury_accounts' in bank and isinstance(
            bank['treasury_accounts'], list
        ):
            bank['treasury_accounts'] = bank['treasury_accounts'][0]
        return bank
    except Exception as e:
        print(e)


async def create_bank_by_id(
    bic: str, bank_info: dict, session, is_archived: bool = False,
):
    """
    Создание в БД записи о новом банке.
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


async def create_milti_banks(bics: set):
    async with get_async_session_context() as session:
        for bic in bics:
            try:
                dadata = await get_bank_by_id(bic)
                await create_bank_by_id(bic, dadata, session)
            except ValueError:
                pass
    return None


if __name__ == "__main__":
    # asyncio.run(get_bank_by_id('004525988'))  # УФК
    # print(asyncio.run(get_bank_by_id('007182108')))

    # asyncio.run(get_bic_list('app/services/config/biclist.txt'))
    asyncio.run(create_milti_banks(BICS))

    # asyncio.run()
