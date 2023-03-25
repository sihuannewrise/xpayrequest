from datetime import date
from typing import Optional, List

from pydantic import BaseModel, Extra, Field, validator, constr
from app.core.models._selectchoice import BankOPFType, EntityStatus
from app.core.settings import variables as var


class BankBase(BaseModel):
    name: Optional[str] = Field(
        ...,
        max_length=160,
        title='Название банка',
        description='Можно загрузить из классификатора по БИК',
    )
    bic: Optional[str] = constr(
        regex='^[0-9]+$',
        min_length=var.BIC_LEN,
        max_length=var.BIC_LEN,
        strip_whitespace=True,
        title='БИК',
    )
    is_archived: Optional[bool] = Field(
        False,
        title='Пометка архивной записи',
        description='По умолчанию значение false',
    )

    address: Optional[str] = Field(max_length=200)
    status: Optional[EntityStatus]
    inn: Optional[str] = constr(
        regex='^[0-9]+$',
        strip_whitespace=True,
    )
    kpp: Optional[str] = constr(
        regex='^[0-9]+$',
        min_length=var.KPP_LEN,
        max_length=var.KPP_LEN,
        strip_whitespace=True,
    )
    actuality_date: Optional[date]
    registration_date: Optional[date]
    liquidation_date: Optional[date]
    correspondent_account: Optional[str] = Field(
        min_length=var.CORR_ACC_LEN,
        max_length=var.CORR_ACC_LEN,
    )
    payment_city: Optional[str] = Field(max_length=50)
    swift: Optional[str] = Field(
        min_length=var.SWIFT_LEN,
        max_length=var.SWIFT_LEN,
    )
    registration_number: Optional[str] = Field(max_length=20)
    treasury_accounts: Optional[str] = Field(
        min_length=20,
        max_length=20,
    )
    opf_type: Optional[BankOPFType]
    description: Optional[str]

    class Config:
        extra = Extra.forbid
        min_anystr_length = 2

    @validator('inn')
    def inn_len_fixed(cls, value):
        if len(value) not in var.INN_LEN:
            raise ValueError(
                f'Длина ИНН должна быть {var.INN_LEN[0]} '
                f'или {var.INN_LEN[1]} знаков!',
            )
        return value


class BankCreate(BankBase):
    name: str = Field(
        ...,
        max_length=160,
        title='Название банка',
        description='Можно загрузить из классификатора по БИК',
    )
    bic: str = constr(
        regex='^[0-9]+$',
        min_length=var.BIC_LEN,
        max_length=var.BIC_LEN,
        strip_whitespace=True,
        title='БИК',
    )
    is_archived: bool = Field(
        False,
        title='Пометка архивной записи',
        description='По умолчанию значение false',
    )


class BankUpdate(BankBase):
    pass


class BankDB(BankBase):
    id: int
    name: str
    bic: str
    is_archived: bool

    address: str
    status: EntityStatus
    inn: str
    kpp: str
    actuality_date: date
    registration_date: date
    liquidation_date: date

    correspondent_account: str
    payment_city: str
    swift: str
    registration_number: str
    treasury_accounts: str
    opf_type: BankOPFType
    description: str

    class Config:
        title = 'Класс со схемой ответа из БД'
        orm_mode = True


class PaginatedBankDB(BaseModel):
    limit: int
    offset: int
    data: List[BankDB]
