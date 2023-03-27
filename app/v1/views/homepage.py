from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", tags=['web'],
            response_class=HTMLResponse,
            summary='Главная страница',
            )
async def home(request: Request):
    """
    ОБРАЗЕЦ

    Отображение главной страницы:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    return templates.TemplateResponse(
        "pages/homepage.html",
        {"request": request},
    )
