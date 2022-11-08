from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.directors import director_router

base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/tables.sql')

app = FastAPI()


app.include_router(director_router)
