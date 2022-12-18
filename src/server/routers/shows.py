import fastapi
from server.sql_base.models import Shows
from server.resolvers.shows import new_show, get_show, get_all_shows, del_show, upd_show
from typing import Any

shows_router = fastapi.APIRouter(prefix='/shows', tags=['Shows'])


@shows_router.get("/")
def start_page():
    return f"Hello new user!"


@shows_router.get("/get/{show_id}/", response_model=Shows | dict)
def get_show_rout(show_id: int) -> Shows | dict:
    return get_show(show_id)


@shows_router.get("/get/", response_model=list[Shows] | dict)
def get_shows_all() -> list[Shows] | dict:
    return get_all_shows()


@shows_router.post("/create/", response_model=int | dict)
def create_show(show: Shows) -> int | dict:
    return new_show(show)


@shows_router.put("/update/{show_id}/", response_model=tuple[Any, Any] | dict)
def update_show(show_id: int, new_data: Shows) -> tuple[Any, Any] | dict:
    return upd_show(show_id, new_data)


@shows_router.delete("/delete/{show_id}/", response_model=tuple[Any, Any] | dict)
def delete_show(show_id) -> tuple[Any, Any] | dict:
    return del_show(show_id)
