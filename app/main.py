from fastapi import FastAPI
from app.core.config import settings
# from app.v1.endpoints.endpoints import router

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)

# app.include_router(router)
