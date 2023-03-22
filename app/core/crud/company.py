from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class DonationCRUD(CRUDBase):

    async def get_user_donations(self, user: User, session: AsyncSession):
        donations = await session.scalars(
            select(self.model).where(
                self.model.user_id == user.id
            )
        )
        return donations.all()


donation_crud = DonationCRUD(Donation)
