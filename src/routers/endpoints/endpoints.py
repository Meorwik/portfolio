
from fastapi import APIRouter, Depends, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

router: APIRouter = APIRouter()
templates = Jinja2Templates(directory="src/templates")
@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})