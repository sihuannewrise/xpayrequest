# from typing import Mapping

# from sqlalchemy.ext.asyncio import AsyncSession

# from app.core.crud.base import CRUDBase as crudbase
# from app.core.exceptions.base import (
#     ObjectNotFoundError,
# )


# async def valid_obj_id(self, obj_id, session: AsyncSession) -> Mapping:
#     obj = await crudbase.get(self, obj_id, session)
#     if not obj:
#         raise ObjectNotFoundError()
#     return obj
