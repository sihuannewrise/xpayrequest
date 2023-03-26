from collections.abc import Mapping

from app.core.crud.base import CRUDBase
from app.core.exceptions.base import ObjectNotFoundError


async def valid_obj_id(model, obj_id: int) -> Mapping:
    obj = await CRUDBase.get(obj_id)
    if not obj:
        raise ObjectNotFoundError()
    return obj
