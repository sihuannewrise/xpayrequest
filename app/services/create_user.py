import asyncio

from contextlib import asynccontextmanager as asyncm
from fastapi_users.exceptions import UserAlreadyExists

from app.core.db import get_async_session
from app.core.user import get_user_db, get_user_manager
from app.core.schemas import UserCreate

get_async_session_context = asyncm(get_async_session)
get_user_db_context = asyncm(get_user_db)
get_user_manager_context = asyncm(get_user_manager)


async def create_user(
    email: str,
    password: str,
    is_superuser: bool = False,
    first_name: str = None,
    patronymic_name: str = None,
    last_name: str = None,
    description: str = None,
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            email=email,
                            password=password,
                            is_superuser=is_superuser,
                            first_name=first_name,
                            patronymic_name=patronymic_name,
                            last_name=last_name,
                            description=description,
                        )
                    )
                    print(f"User created {user}")
    except UserAlreadyExists:
        print(f"User {email} already exists")


if __name__ == "__main__":
    asyncio.run(create_user("king.arthur@camelot.bt", "guinevere"))
