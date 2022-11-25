import fastapi
from sql_base import models
from resolvers import new_staff, get_staff


staff_router = fastapi.APIRouter()


@staff_router.get("/")
def start_page():
    return f"Hello world"


@staff_router.get("/staff")
def get_staff_rout(staff: models.StaffSearch):
    staff = get_staff(staff)
    return staff


@staff_router.post("/staff")
def create_staff(staff: models.Staff):
    new_id = new_staff(staff)
    return f"{{code: 201, id: {new_id}}}"
