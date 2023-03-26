from uuid import UUID
from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.core.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(
        auth_backend, requires_verification=True),
    prefix='/auth/web',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(
        UserRead, UserUpdate, requires_verification=True),
    prefix='/users',
    tags=['users'],
)


@router.delete(
    '/users/{id}', tags=['users'], deprecated=True,
)
def delete_user(id: UUID):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        status_code=405,
        detail="Удаление пользователей запрещено!"
    )
