from fastapi.staticfiles import StaticFiles

from src.data.config import AppConfig, MetaData
from typing import Final, List, Union
from fastapi.templating import Jinja2Templates
from main import app
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

app.mount("src/static", StaticFiles(directory="static"), name="static")

config: Final[AppConfig] = AppConfig()
meta: Final[MetaData] = MetaData()