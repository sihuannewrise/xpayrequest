from typing import Mapping

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.base import CRUDBase as crudbase
from app.core.dependencies.base import check_obj_not_exist
from app.core.exceptions.base import (
    ObjectAlreadyExistsError,
)
from app.core.models.bank import Bank


async def check_bank_not_exist(
    bic_val: str,
    session: AsyncSession,
) -> Mapping:
    bank = await check_obj_not_exist(Bank, 'bic', bic_val)
    if bank is not None:
        raise ObjectAlreadyExistsError()
    return bank
