from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.bank import bank_crud
from app.core.db import get_async_session
from app.core.schemas.bank import (
    BankCreate, BankDB, BankUpdate,
)
from app.core.user import current_superuser, current_user
from app.core.models import Bank
from app.core.exceptions.bank import BankAlreadyExistsError, BankNotFoundError
from app.v1.validators.bank import check_name_duplicate

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
) -> list[Bank]:
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
    await check_name_duplicate(bank.name, session)
    new_bank = await bank_crud.create_bank(bank, session)
    return new_bank


@router.patch(
    '/{bic}',
    response_model=BankDB,
    response_model_exclude_none=True,
    response_model_exclude_defaults=True,
    response_model_exclude_unset=True,
    dependencies=[Depends(current_superuser)],
    summary='Обновление полей банка',
)
async def partially_update_bank(
    bic: str,
    upd_data: BankUpdate,
    session: AsyncSession = Depends(get_async_session),
) -> Bank:
    """
    Только для суперпользователей.
    Обновление данных по БИК.
    """
    bank = await bank_crud.get_bank_by_bic(bic, session)
    if bank is None:
        raise BankNotFoundError()
    if upd_data.name is not None:
        await check_name_duplicate(upd_data.name, session)
    bank = await bank_crud.update(bank, upd_data, session)
    return bank
