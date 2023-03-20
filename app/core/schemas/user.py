from uuid import UUID
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[UUID]):
    description: str


class UserCreate(schemas.BaseUserCreate):
    description: Optional[str]


class UserUpdate(schemas.BaseUserUpdate):
    description: Optional[str]
