# schemas for supplementary models:
SUPP_SCHEMAS = [
    'BankAccountType',
    'PaymentType',
    'KFP',
    'PayerStatus',
    'KBK',
    'OKTMO',
    'Prepayment',
    'PaymentStatus',
    'PaymentVerdict',
]

from typing import Optional
from pydantic import BaseModel, Field, validator


class SuppBase(BaseModel):
    name: Optional[str] = Field(
        None,
        max_length=50,
    )
    description: Optional[str | None] = None

    class Config:
        min_anystr_length = 2


class SuppObjectCreate(SuppBase):
    __metaclass__ = type
    name: str = Field(
        max_length=50,
    )


class SuppObjectUpdate(SuppBase):
    __metaclass__ = type

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Название объекта не может быть пустым!')
        return value


class SuppObjectDB(SuppBase):
    __metaclass__ = type

    id: int

    class Config:
        orm_mode = True


for schema in SUPP_SCHEMAS:
        
