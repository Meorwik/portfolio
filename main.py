from src.routers.endpoints.endpoints import router
from fastapi import FastAPI


app = FastAPI()
app.include_router(router)