import asyncio
from pydantic import EmailStr

from contextlib import asynccontextmanager
from fastapi_users.exceptions import UserAlreadyExists

from app.core.config import settings
from app.core.db import get_async_session
from app.core.user import get_user_db, get_user_manager
from app.core.schemas.user import UserCreate

get_async_session_context = asynccontextmanager(get_async_session)
get_user_db_context = asynccontextmanager(get_user_db)
get_user_manager_context = asynccontextmanager(get_user_manager)


async def create_user(
    email: EmailStr,
    password: str,
    is_superuser: bool = False,
    description: str = None,
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    await user_manager.create(
                        UserCreate(
                            email=email,
                            password=password,
                            is_superuser=is_superuser,
                            description=description,
                        )
                    )
    except UserAlreadyExists:
        pass


async def create_first_superuser():
    if (settings.first_superuser_email is not None
            and settings.first_superuser_password is not None):
        await create_user(
            email=settings.first_superuser_email,
            password=settings.first_superuser_password,
            is_superuser=True,
            description='autocreated superuser'
        )


if __name__ == "__main__":
    # asyncio.run(create_user("king.arthur@camelot.bt", "guinevere"))
    asyncio.run(create_first_superuser())
