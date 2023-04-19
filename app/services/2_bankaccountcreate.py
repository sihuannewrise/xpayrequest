# command to run this script from root dir:  python -m app.services.2_bankaccountcreate  # noqa

import os
import asyncio
import aiofiles

from contextlib import asynccontextmanager

from sqlalchemy import select
from app.core.db import get_async_session
from app.core.models import (
    Bank, BankAccount, CaAccountMapping, Currency,
)

from app.services.config.accounts import ACCOUNTS
from app.services.config.currency_ids import CURRENCY_IDS
from app.services.config.mapping import RUBLE_CODE

get_async_session_context = asynccontextmanager(get_async_session)


async def get_account_list(filename):
    accounts = {}
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            bic, inn, account = line.strip().split()
            if account not in accounts:
                accounts.update({account: {bic: set([inn])}})
            else:
                accounts[account][bic].add(inn)
        # for el, val in accounts.items():
        #     print(f"'{el}': {val}")
        for acc, info in accounts.items():
            for bic, inn in info.items():
                print(f"'{acc}': {{'{bic}': {list(inn)}}},")


async def write_currencies_to_file():
    """
    Utility writes all currencies (name, id) from DB to a dictionary.
    """
    async with get_async_session_context() as session:
        currency_ids = await session.execute(
            select(Currency.name, Currency.id))
        currency_ids = currency_ids.all()
    async with aiofiles.open(
        'app/services/config/currency_ids.py', mode='w'
    ) as file:
        my_ids = {}
        for id in currency_ids:
            my_ids[id[0]] = id[1]
        await file.write(f'CURRENCY_IDS = {my_ids}\n')


async def check_duplicate_by_field(model, field, field_value, session):
    col = getattr(model, field)
    duplicate = await session.scalar(select(col).where(col == field_value))
    if duplicate is not None:
        raise IndexError(
            f'Значение {field}=\033[1m{field_value}\033[0m уже в таблице '
            f'\033[1m{model.__name__.lower()}\033[0m !'
        )


async def add_bank_account(model, acc_num: str, bic: str, session):
    try:
        await check_duplicate_by_field(model, 'account', acc_num, session)
    except IndexError as e:
        print(e)
    else:
        try:
            await check_duplicate_by_field(Bank, 'bic', acc_num, session)
        except IndexError as e:
            print(e)
        else:
            currency_code = acc_num[5:8]
            if currency_code not in CURRENCY_IDS:
                currency_code = RUBLE_CODE
            acc_model = model(
                account=acc_num,
                bank_bic=bic,
                currency_id=CURRENCY_IDS[currency_code],
                description=f'autoloaded by {os.path.basename(__file__)}'
            )
            session.add(acc_model)
            await session.commit()


async def add_caaccount_mapping(model, acc_num: str, inn: str, session):
    try:
        ca_account = await session.scalar(select(model.id).where(
            model.ca_account == acc_num,
            model.ca_inn == inn,
        ))
        if ca_account is not None:
            raise ValueError(
                f'inn==\033[1m{inn}\033[0m account=\033[1m{acc_num}\033[0m '
                f'уже в таблице \033[1m{model.__name__.lower()}\033[0m !'
            )
    except IndexError as e:
        print(e)
    else:
        mapping_model = model(
            ca_inn=inn,
            ca_account=acc_num,
            is_default=False,
            description=f'autoloaded by {os.path.basename(__file__)}'
        )
        session.add(mapping_model)
        await session.commit()


async def add_multi_records(data: dict) -> None:
    async with get_async_session_context() as session:
        # await write_currencies_to_file()
        for account, vals in data.items():
            for bic, inn_list in vals.items():
                try:
                    await add_bank_account(
                        BankAccount, account, bic, session)
                except ValueError as e:
                    print(e)
                else:
                    for inn in inn_list:
                        try:
                            await add_caaccount_mapping(
                                CaAccountMapping, account, inn, session)
                        except ValueError as e:
                            print(e)


if __name__ == "__main__":
    # asyncio.run(get_account_list('app/services/config/accounts.txt'))
    # asyncio.run(write_ids_to_file())

    asyncio.run(add_multi_records(ACCOUNTS))
