from datetime import date
from typing import Optional, List

from pydantic import BaseModel, Field, validator
from app.core.models._selectchoice import BankOPFType, EntityStatus
from app.core.settings import variables as var


class BankBase(BaseModel):
    name: Optional[str] = Field(
        None,
        max_length=160,
        title='Название банка',
    )
    bic: Optional[str] = Field(
        None,
        regex=r'^[0-9]+$',
        min_length=var.BIC_LEN,
        max_length=var.BIC_LEN,
        title='БИК',
    )
    is_archived: Optional[bool] = Field(
        False,
        include_in_schema=False,
    )

    address: Optional[str] = Field(None, max_length=200)
    status: Optional[EntityStatus] = Field(None,)
    inn: Optional[str] = Field(
        None,
        regex=r'^[0-9]+$',
        min_length=var.INN_LEN[0],
        max_length=var.INN_LEN[1],
        title='ИНН банка',
    )
    kpp: Optional[str] = Field(
        None,
        regex=r'^[0-9]+$',
        min_length=var.KPP_LEN,
        max_length=var.KPP_LEN,
        title='КПП банка',
    )
    actuality_date: Optional[date] = Field(None,)
    registration_date: Optional[date] = Field(None,)
    liquidation_date: Optional[date] = Field(None,)
    correspondent_account: Optional[str] = Field(
        None,
        regex=r'^[0-9]+$',
        min_length=var.CORR_ACC_LEN,
        max_length=var.CORR_ACC_LEN,
    )
    payment_city: Optional[str] = Field(None, max_length=50)
    swift: Optional[str] = Field(
        None,
        min_length=var.SWIFT_LEN,
        max_length=var.SWIFT_LEN,
    )
    registration_number: Optional[str] = Field(None, max_length=20)
    treasury_accounts: Optional[str] = Field(
        None,
        regex=r'^[0-9]+$',
        min_length=20,
        max_length=20,
    )
    opf_type: Optional[BankOPFType] = Field(None,)
    description: Optional[str] = Field(None,)

    # class Config:
    #     min_anystr_length = 2


class BankCreate(BankBase):
    name: str = Field(
        max_length=160,
        title='Название банка',
    )
    bic: str = Field(
        regex=r'^[0-9]+$',
        min_length=var.BIC_LEN,
        max_length=var.BIC_LEN,
        title='БИК',
    )
    is_archived: bool = Field(
        False,
        include_in_schema=False,
    )

    class Config:
        schema_extra = {
            'example': {
               'name': 'ПАО Сбербанк',
               'bic': '044525225',
               'correspondent_account': '30101810400000000225',
               'payment_city': 'г Москва',
               'opf_type': 'банк',
               'status': 'действующая',
               'address': 'г Москва, ул Вавилова, д 19'
            }
        }


class BankUpdate(BankBase):
    bic: Optional[str] = Field(
        example='044525225',
        include_in_schema=False,
    )

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя банка не может быть пустым!')
        return value

    class Config:
        schema_extra = {
            'example': {
               'inn': '7707083893',
               'kpp': '773601001',
               'address': 'г. Москва, ул. Вавилова, дом 19'
            }
        }


class BankDB(BankBase):
    bic: str
    name: str
    is_archived: bool = False
    address: str | None = None
    status: EntityStatus | None = None
    correspondent_account: str | None = None
    payment_city: str | None = None

    inn: str | None = None
    kpp: str | None = None
    actuality_date: date | None = None
    registration_date: date | None = None
    liquidation_date: date | None = None
    swift: str | None = None
    registration_number: str | None = None
    treasury_accounts: str | None = None
    opf_type: BankOPFType | None = None
    description: str | None = None

    class Config:
        orm_mode = True


class PaginatedBankDB(BaseModel):
    limit: int
    offset: int
    data: List[BankDB]
