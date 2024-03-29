from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from app.core.config import settings

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get(
    "/",
    response_class=HTMLResponse,
    summary='Главная страница',
)
async def home(request: Request):
    """
    ОБРАЗЕЦ

    Отображение главной страницы:

    - **name**: имя
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    title = settings.app_title
    return templates.TemplateResponse(
        "pages/homepage.html",
        {
            'request': request,
            'title': title,
        },
    )
