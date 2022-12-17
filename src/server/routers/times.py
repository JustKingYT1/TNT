import fastapi
from server.sql_base.models import ShowsTime
from server.resolvers.times import new_time, del_time, upd_time, get_all_times, get_time
from typing import Any

times_router = fastapi.APIRouter(prefix='/times', tags=['Times'])


@times_router.get("/")
def start_page():
    return f"Hello new user!"


@times_router.get("/get/{time_id}/", response_model=ShowsTime | dict)
def get_time_rout(time_id: int) -> ShowsTime | dict:
    return get_time(time_id)


@times_router.get("/get/", response_model=list[ShowsTime] | dict)
def get_times_all() -> list[ShowsTime] | dict:
    return get_all_times()


@times_router.post("/create/", response_model=None | dict)
def create_time(time: ShowsTime) -> None | dict:
    return new_time(time)


@times_router.put("/update/{time_id}/", response_model=None | dict)
def update_time(time_id: int, new_data: ShowsTime) -> None | dict:
    return upd_time(time_id, new_data)


@times_router.delete("/delete/{time_id}/", response_model=tuple[Any, Any] | dict)
def delete_time(time_id) -> tuple[Any, Any] | dict:
    return del_time(time_id)
