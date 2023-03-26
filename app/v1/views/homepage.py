from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", tags=['web'], response_class=HTMLResponse,)
async def home(request: Request):
    return templates.TemplateResponse(
        "pages/homepage.html",
        {"request": request},
    )
