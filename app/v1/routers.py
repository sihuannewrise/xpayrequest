from fastapi import APIRouter
from app.v1.endpoints import user_router
from app.v1.views import web_router

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(web_router)
