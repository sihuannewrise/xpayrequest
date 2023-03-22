from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.base import CRUDBase
from app.core.models.bank import Bank


class BankCRUD(CRUDBase):

    async def get_bank_by_name(
        self,
        bank_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        db_bank_id = await session.scalar(
            select(Bank).where(
                Bank.name == bank_name
            )
        )
        return db_bank_id


bank_crud = BankCRUD(Bank)
