from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.bank import bank_crud
from app.core.db import get_async_session
from app.core.schemas.bank import (
    BankCreate, BankDB,
)
from app.core.user import current_superuser, current_user
from app.core.models import Bank
from app.core.exceptions.bank import BankAlreadyExistsError

router = APIRouter()


@router.get(
    '/',
    response_model=list[BankDB],
    response_model_exclude_none=True,
    response_model_exclude_defaults=True,
    response_model_exclude_unset=True,
    dependencies=[Depends(current_user)],
    summary='Список банков',
    response_description='Список всех банков из БД',
)
async def get_all_banks(
    session: AsyncSession = Depends(get_async_session),
) -> List[Bank]:
    """
    Просмотр списка всех банков.
    Доступно для всех зарегистрированных пользователей.
    """
    return await bank_crud.get_multi(session=session)


@router.post(
    '/',
    response_model=BankDB,
    response_model_exclude_none=True,
    response_model_exclude_defaults=True,
    response_model_exclude_unset=True,
    dependencies=[Depends(current_superuser)],
    summary='Создание нового банка',
    response_description='В случае успешного создания '
                         'возвращаются данные вновь созданного банка.',
)
async def create_new_bank(
    bank: BankCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Bank:
    """
    Только для суперпользователей.

    Создает банк, обязательные поля:
     - **name** - имя банка;
     - **bic** - БИК банка.
    """
    bic = await bank_crud.get_bank_by_bic(bank.bic, session)
    if bic is not None:
        raise BankAlreadyExistsError()
    new_bank = await bank_crud.create_bank(bank, session)
    return new_bank
