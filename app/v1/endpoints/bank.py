from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.bank import bank_crud
from app.core.db import get_async_session
from app.core.schemas.bank import (
    BankCreate, BankDB,
)
from app.core.user import current_superuser
# from app.core.dependencies.bank import check_bank_not_exist

router = APIRouter()


@router.get(
    '/',
    response_model=list[BankDB],
    response_model_exclude_none=True,
    summary='Список всех банков',
    response_description='Список банков из БД',
)
async def get_all_banks(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Доступно для всех посетителей.
    Просмотр списка всех банков.
    """
    return await bank_crud.get_multi(session=session)


@router.post(
    '/',
    response_model=BankDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
    summary='Создание нового банка',
    response_description='Данные вновь созданного банка',
)
async def create_new_bank(
    bank: BankCreate,
    session: AsyncSession = Depends(get_async_session),
):
    # """
    # Только для суперпользователей.

    # Создает банк, обязательные поля:
    #  - **name** - имя банка;
    #  - **bic** - БИК банка.
    # """
    new_bank = await bank_crud.create_bank(bank, session)
    return new_bank
