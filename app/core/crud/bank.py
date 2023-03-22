from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.base import CRUDBase
from app.core.models.bank import Bank


class BankCRUD(CRUDBase):

    async def get_bank_by_name(
        self,
        bank_name: str,
        session: AsyncSession,
    ):
        bank = await session.scalar(
            select(Bank).where(
                Bank.name == bank_name
            )
        )
        return bank


bank_crud = BankCRUD(Bank)
