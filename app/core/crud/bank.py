from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.crud.base import CRUDBase
from app.core.models.bank import Bank
from app.core.exceptions.bank import BankAlreadyExistsError, BankNotFoundError
from app.core.schemas.bank import BankCreate, BankDB, BankUpdate


class BankCRUD(CRUDBase):
    async def get_bank_by_id(
        bank_id: int,
        session: AsyncSession,
    ) -> Bank:
        bank = await session.scalar(select(Bank).where(Bank.id == bank_id))
        if bank is None:
            raise BankNotFoundError
        return bank

    async def create_bank(
        bank_info: BankCreate,
        session: AsyncSession,
    ) -> Bank:
        query = select(Bank).where(Bank.bic == bank_info.bic)
        bank_details = await session.scalar(query)
        if bank_details is not None:
            raise BankAlreadyExistsError

        obj_in_data = bank_info.dict()
        new_bank_info = Bank(**obj_in_data)
        session.add(new_bank_info)
        await session.commit()
        await session.refresh(new_bank_info)
        return new_bank_info

    async def update_bank(
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
