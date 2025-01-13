from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import lifespan

#
# from routers.transistor import router as transistor_router
# from routers.users import router as task_router
#
#
from fastapi import FastAPI, Request
#
# from db.database import create_tables, delete_tables


app = FastAPI()
# app.include_router(transistor_router)
# app.include_router(task_router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="public"))

@app.get("/")
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("main.html", {"request": request, "title": "Главная"})