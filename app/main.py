from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import settings
from app.v1.endpoints import user_router
# from app.services.create_user import create_first_superuser

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user_router)


# @app.on_event('startup')
# async def startup():
#     await create_first_superuser()
