from datetime import date
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator
from app.core.models._selectchoice import BankOPFType, EntityStatus


class BankBase(BaseModel):
    name: Optional[str] = Field(max_length=160)
    bic: Optional[str]
    is_archived: Optional[bool]

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя не может быть пустым!')
        return value

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class BankCreate(BankBase):
    name: str
    bic: str
    is_archived: bool


class BankUpdate(BankBase):
    name: str
    bic: str
    is_archived: bool


class BankDB(BankBase):
    id: int
    description: str

    name: str = Field(max_length=160)
    address: str = Field(max_length=200)
    status: EntityStatus
    inn: str = Field(max_length=12)
    kpp: str = Field(max_length=9)
    actuality_date: date
    registration_date: date
    liquidation_date: date
    is_archived: bool

    bic: str
    correspondent_account: str = Field(max_length=20)
    payment_city: str = Field(max_length=50)
    swift: str = Field(max_length=11)
    registration_number: str = Field(max_length=20)
    treasury_accounts: str = Field(max_length=20)
    opf_type: BankOPFType

    class Config:
        orm_mode = True
