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


# async def check_bank_before_delete(
#     bank_id: int,
#     session: AsyncSession
# ) -> CharityProject:
#     bank = await check_bank_exists(
#         bank_id=bank_id, session=session
#     )
#     if bank.invested_amount > 0:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail=('В проект были внесены средства, не подлежит удалению!')
#         )
#     return bank


# async def check_bank_before_update(
#     bank_id: int,
#     bank_in: CharityProjectUpdate,
#     session: AsyncSession,
# ) -> CharityProject:
#     bank = await check_bank_exists(
#         bank_id=bank_id, session=session
#     )
#     if bank.close_date is not None:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail='Закрытый проект нельзя редактировать!'
#         )
#     full_amount_update_value = bank_in.full_amount
#     if (full_amount_update_value and
#        bank.invested_amount > full_amount_update_value):
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail='Нельзя установить требуемую cумму меньше уже вложенной'
#         )
#     name_update_value = bank_in.name
#     await check_bank_name_duplilcate(
#         bank_name=name_update_value, session=session
#     )
#     return bank
