import fastapi
from server.sql_base.models import Schedules_id, ScheduleOfShows
from server.resolvers.schedules import new_schedule_id, del_schedule_id, get_all_schedules_id, get_schedule_id, upd_schedule_id


staff_router = fastapi.APIRouter(prefix='/schedules', tags=['Staff'])

times_router = fastapi.APIRouter(prefix='schedules/times')


@staff_router.get("/")
def start_page():
    return f"Hello new user!"


@staff_router.get("/get/{staff_id}/", response_model=Staff | dict)
def get_staff_rout(staff_id: int) -> Staff | dict:
    return get_staff(staff_id)


@staff_router.get("/get/")
def get_staff_all() -> list[Staff] | dict:
    return get_all_staff()


@staff_router.post("/create/", response_model=int | dict)
def create_staff(staff: Staff) -> int | dict:
    return new_staff(staff)


@staff_router.put("/update/{staff_id}/", response_model=None | dict)
def update_staff(staff_id: int, new_data: Staff) -> None | dict:
    return upd_staff(staff_id, new_data)


@staff_router.delete("/delete/{staff_id}/", response_model=None | dict)
def delete_staff(staff_id) -> None | dict:
    return del_staff(staff_id)
