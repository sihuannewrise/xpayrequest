from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.bank import bank_crud
from app.core.models.bank import Bank


async def check_bank_exists(
    bank_bic: str,
    session: AsyncSession
) -> Bank:
    bank = await bank_crud.get_obj_by_pk(bank_bic, session)
    if bank is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Банк с указанным БИК не найден!'
        )
    return bank


async def check_name_duplicate(
    bank_name: str,
    session: AsyncSession,
) -> None:
    bank = await bank_crud.get_obj_by_name(
        obj_name=bank_name,
        session=session,
    )
    if bank is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Банк с таким названием уже существует!'
        )
