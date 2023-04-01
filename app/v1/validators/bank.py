from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.bank import bank_crud
# from app.core.models.bank import Bank
# from app.core.schemas.bank import BankUpdate


# async def check_charity_project_exists(
#     charity_project_id: int,
#     session: AsyncSession
# ) -> CharityProject:
#     charity_project = await charity_project_crud.get(
#         obj_id=charity_project_id, session=session
#     )
#     if charity_project is None:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND,
#             detail='Проекта с указанным id не существует!'
#         )
#     return charity_project


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
            detail='Банк с таким именем уже существует!'
        )


# async def check_charity_project_before_delete(
#     charity_project_id: int,
#     session: AsyncSession
# ) -> CharityProject:
#     charity_project = await check_charity_project_exists(
#         charity_project_id=charity_project_id, session=session
#     )
#     if charity_project.invested_amount > 0:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail=('В проект были внесены средства, не подлежит удалению!')
#         )
#     return charity_project


# async def check_charity_project_before_update(
#     charity_project_id: int,
#     charity_project_in: CharityProjectUpdate,
#     session: AsyncSession,
# ) -> CharityProject:
#     charity_project = await check_charity_project_exists(
#         charity_project_id=charity_project_id, session=session
#     )
#     if charity_project.close_date is not None:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail='Закрытый проект нельзя редактировать!'
#         )
#     full_amount_update_value = charity_project_in.full_amount
#     if (full_amount_update_value and
#        charity_project.invested_amount > full_amount_update_value):
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail='Нельзя установить требуемую cумму меньше уже вложенной'
#         )
#     name_update_value = charity_project_in.name
#     await check_charity_project_name_duplilcate(
#         charity_project_name=name_update_value, session=session
#     )
#     return charity_project
