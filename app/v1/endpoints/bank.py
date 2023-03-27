from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.bank import bank_crud
from app.core.db import get_async_session
from app.core.schemas.bank import (
        BankCreate, BankDB,
)
from app.core.user import current_superuser

router = APIRouter()


@router.get(
    '/',
    response_model=list[BankDB],
    response_model_exclude_none=True,
    summary='Список всех банков'
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
    summary='Создать банк',
)
async def create_new_bank(
    bank: BankCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперпользователей.
    Создает банк.
     - **name** - имя банка;
     - **bic** - БИК банка;
     - **description** - описание банка.
    """
    new_bank = await bank_crud.create_bank(bank, session)
    return new_bank
