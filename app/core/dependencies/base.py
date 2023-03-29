from typing import Mapping

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.base import CRUDBase as crudbase
from app.core.exceptions.base import (
    ObjectNotFoundError, ObjectAlreadyExistsError,
)


async def valid_obj_id(self, obj_id, session: AsyncSession) -> Mapping:
    obj = await crudbase.get(self, obj_id, session)
    if not obj:
        raise ObjectNotFoundError()
    return obj


async def check_obj_not_exist(
    model, field, obj_id, session: AsyncSession,
):
    obj = await session.scalar(
        select(model).where(model[field] == obj_id)
    )
    if obj is not None:
        raise ObjectAlreadyExistsError(f'{model}')
    return None
