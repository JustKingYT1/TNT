from typing import Any

import fastapi

from server.sql_base.models import SchedulesID, ScheduleOfShows
from server.resolvers.schedules import new_schedule_id, del_schedule_id, get_all_schedules_id, get_schedule_id, upd_schedule_id, get_schedule, get_all_schedules

schedules_id_router = fastapi.APIRouter(prefix='/schedules/id', tags=['SchedulesID'])

schedules_router = fastapi.APIRouter(prefix='/schedules', tags=['Schedules'])


@schedules_router.get("/")
def start_page_1():
    return f"Hello new user!"


@schedules_id_router.get("/")
def start_page_2():
    return f"Hello new user!"


@schedules_id_router.get("/get/{schedule_id}/", response_model=SchedulesID | dict)
def get_schedule_id_rout(schedule_id: int) -> SchedulesID | dict:
    return get_schedule_id(schedule_id)


@schedules_id_router.get("/get/", response_model=list[SchedulesID] | dict)
def get_schedules_id_all() -> list[SchedulesID] | dict:
    return get_all_schedules_id()


@schedules_id_router.post("/create/", response_model=int | dict)
def create_schedule(schedule: SchedulesID) -> int | dict:
    return new_schedule_id(schedule)


@schedules_id_router.put("/update/{schedule_id}/", response_model=None | dict)
def update_schedule(schedule_id: int, new_data: SchedulesID) -> None | dict:
    return upd_schedule_id(schedule_id, new_data)


@schedules_id_router.delete("/delete/{schedule_id}/", response_model=tuple[Any, Any] | dict)
def delete_schedule(schedule_id) -> tuple[Any, Any] | dict:
    return del_schedule_id(schedule_id)


@schedules_router.get("/get/{schedule_id}/", response_model=ScheduleOfShows | dict)
def get_schedule_rout(schedule_id: int) -> ScheduleOfShows | dict:
    return get_schedule(schedule_id)


@schedules_router.get("/get/", response_model=list[ScheduleOfShows] | dict)
def get_schedules_all() -> list[ScheduleOfShows] | dict:
    return get_all_schedules()
