from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.user import User
from app.core.settings import variables as var


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get_obj_by_name(
        self, obj_name, session: AsyncSession,
    ) -> Optional[int | str]:
        db_obj_id = await session.scalar(
            select(self.model).where(
                self.model.name == obj_name
            )
        )
        return db_obj_id

    async def get_obj_by_pk(
        self, pk, session: AsyncSession,
    ) -> Optional[int | str]:
        db_obj = await session.get(self.model, pk)
        return db_obj

    async def get_multi(
        self, session: AsyncSession,
        limit: int = var.PAG_LIMIT,
        offset: int = var.PAG_OFFSET,
    ):
        db_objs = await session.scalars(
            select(self.model).offset(offset).limit(limit))
        return db_objs.all()

    async def create(
        self, obj_in, session: AsyncSession, user: Optional[User] = None
    ):
        obj_in_data = obj_in.dict()
        if user is not None:
            obj_in_data['user_id'] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(self, db_obj, obj_in, session: AsyncSession):
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            for field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(self, db_obj, session: AsyncSession):
        await session.delete(db_obj)
        await session.commit()
        return db_obj
