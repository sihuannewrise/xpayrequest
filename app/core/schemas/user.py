from uuid import UUID
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[UUID]):
    first_name: str
    patronymic_name: str
    last_name: str
    description: str


class UserCreate(schemas.BaseUserCreate):
    first_name: Optional[str]
    patronymic_name: Optional[str]
    last_name: str
    description: Optional[str]


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    patronymic_name: Optional[str]
    last_name: Optional[str]
    description: Optional[str]
