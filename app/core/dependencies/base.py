from typing import Mapping
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.base import CRUDBase
from app.core.exceptions.base import ObjectNotFoundError


async def valid_obj_id(model, obj_id: int, session: AsyncSession) -> Mapping:
    obj = await CRUDBase.get(model, obj_id, session)
    if not obj:
        raise ObjectNotFoundError()
    return obj
