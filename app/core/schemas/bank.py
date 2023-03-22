from datetime import date
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator, constr
from app.core.models._selectchoice import BankOPFType, EntityStatus


class BankBase(BaseModel):
    name: Optional[str] = Field(max_length=160)
    bic: Optional[str] = constr(
        regex='^[0-9]+$',
        min_length=9,
        max_length=9,
        strip_whitespace=True,
    )
    is_archived: Optional[bool] = Field(False)

    address: Optional[str] = Field(max_length=200)
    status: Optional[EntityStatus]
    inn: Optional[str] = constr(
        regex='^[0-9]+$',
        min_length=10,
        max_length=12,
        strip_whitespace=True,
    )
    kpp: Optional[str] = constr(
        regex='^[0-9]+$',
        min_length=9,
        max_length=9,
        strip_whitespace=True,
    )
    actuality_date: date
    registration_date: date
    liquidation_date: date

    correspondent_account: str = Field(max_length=20)
    payment_city: str = Field(max_length=50)
    swift: str = Field(max_length=11)
    registration_number: str = Field(max_length=20)
    treasury_accounts: str = Field(max_length=20)
    opf_type: BankOPFType
    description: str

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя не может быть пустым!')
        return value


class BankCreate(BankBase):
    name: str = Field(max_length=160)
    bic: str = constr(
        regex='^[0-9]+$',
        min_length=9,
        max_length=9,
        strip_whitespace=True,
    )
    is_archived: bool = Field(False)


class BankUpdate(BankBase):
    pass


class BankDB(BankBase):
    id: int
    name: str
    bic: str
    is_archived: bool

    address: str = Field(max_length=200)
    status: EntityStatus
    inn: str = Field(max_length=12)
    kpp: str = Field(max_length=9)
    actuality_date: date
    registration_date: date
    liquidation_date: date

    correspondent_account: str = Field(max_length=20)
    payment_city: str = Field(max_length=50)
    swift: str = Field(max_length=11)
    registration_number: str = Field(max_length=20)
    treasury_accounts: str = Field(max_length=20)
    opf_type: BankOPFType
    description: str

    class Config:
        orm_mode = True
