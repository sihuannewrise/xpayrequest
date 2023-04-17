# command to run this script from root dir:  python -m app.services.bankaccountcreate  # noqa

import os
import asyncio
import aiofiles
from datetime import datetime as dt
from contextlib import asynccontextmanager

from sqlalchemy import select
from app.services.dadata import dd_find_by_id
from app.core.db import get_async_session
from app.core.models.bank import Bank

# from app.services.config.listbic import BICS

get_async_session_context = asynccontextmanager(get_async_session)


async def get_account_list(filename):
    accounts = {}
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            bic, inn, account = line.strip().split()
            if account not in accounts:
                accounts.update({account: {inn: bic}})
            else:
                accounts[account].update({inn: bic})
        for acc, info in accounts.items():
            print(acc)
            for k, v in info.items():
                print(k, v)


async def check_no_bic_duplicate(bic: str, session):
    bank = await session.get(Bank, bic)
    if bank is not None:
        raise ValueError(
            f'БИК \033[1m{bic}\033[0m уже в таблице '
            f'\033[1m{Bank.__name__.lower()}\033[0m !'
        )


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
    asyncio.run(get_account_list('app/services/config/accounts.txt'))
