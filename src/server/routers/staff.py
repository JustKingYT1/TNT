import fastapi
from sql_base import models
from server.resolvers import new_staff, get_staff, upd_staff, del_staff


staff_router = fastapi.APIRouter()


@staff_router.get("/")
def start_page():
    return f"Hello new user!"


@staff_router.get("/staff/", response_model=models.StaffSearch)
def get_staff_rout(staff: models.StaffSearch) -> list[models.Staff]:
    return get_staff(staff)


@staff_router.post("/staff/", response_model=models.Staff | dict)
def create_staff(staff: models.Staff) -> models.Staff | dict:
    return new_staff(staff)


@staff_router.put("/staff/{staff_id}", response_model=None)
def update_staff(staff_id: int, new_data: models.Staff) -> None:
    return upd_staff(staff_id, new_data)


@staff_router.delete("/staff/{staff_id}", response_model=None)
def delete_staff(staff_id) -> None:
    return del_staff(staff_id)
