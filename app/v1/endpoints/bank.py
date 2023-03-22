from fastapi import APIRouter

from app.core.crud.bank import bank_crud
from app.core.schemas.bank import BankCreate

router = APIRouter()


@router.post('/banks/')
async def create_new_bank(
        bank: BankCreate,
):
    new_bank = await bank_crud.create(bank)
    return new_bank
