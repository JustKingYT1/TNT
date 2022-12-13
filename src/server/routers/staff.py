import fastapi
from server.sql_base.models import Staff, StaffSearch
from server.resolvers.staff import new_staff, get_staff, upd_staff, del_staff


staff_router = fastapi.APIRouter(prefix='/staff', tags=['Staff'])


@staff_router.get("/")
def start_page():
    return f"Hello new user!"


@staff_router.get("/staff/", response_model=list[Staff])
def get_staff_rout(staff: StaffSearch) -> list[Staff] | dict:
    return get_staff(staff)


@staff_router.post("/staff/", response_model=int | dict)
def create_staff(staff: Staff) -> int | dict:
    return new_staff(staff)


@staff_router.put("/staff/{staff_id}", response_model=None)
def update_staff(staff_id: int, new_data: Staff) -> None:
    return upd_staff(staff_id, new_data)


@staff_router.delete("/staff/{staff_id}", response_model=None)
def delete_staff(staff_id) -> None:
    return del_staff(staff_id)
