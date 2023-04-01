from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.base import CRUDBase
from app.core.models.bank import Bank
from app.core.schemas.bank import BankCreate, BankDB, BankUpdate


class BankCRUD(CRUDBase):
    async def get_bank_by_bic(
        self, bic: str, session: AsyncSession,
    ) -> Optional[str]:
        query = select(Bank.bic).where(Bank.bic == bic)
        bic = await session.scalar(query)
        return bic

    async def create_bank(
        self, bank: BankCreate, session: AsyncSession,
    ) -> Bank:
        bank_data = bank.dict()
        new_bank = Bank(**bank_data)
        session.add(new_bank)
        await session.commit()
        await session.refresh(new_bank)
        return new_bank

    async def update_bank(
        self,
        bank_db: BankDB,
        update_info: BankUpdate,
        session: AsyncSession,
    ) -> Bank:
        bank_data = jsonable_encoder(bank_db)
        update_data = update_info.dict(exclude_unset=True)
        for field in bank_data:
            for field in update_data:
                setattr(bank_db, field, update_data[field])
        session.add(bank_db)
        await session.commit()
        await session.refresh(bank_db)
        return bank_db


bank_crud = BankCRUD(Bank)
