from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.core.config import settings
from app.v1.routers import main_router
from app.services.create_user import create_first_superuser

app = FastAPI(title=settings.app_title,
              description=settings.app_description,)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()
