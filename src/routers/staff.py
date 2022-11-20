import fastapi
from sql_base import models
from resolvers import new_staff, get_staff


staff_router = fastapi.APIRouter()


@staff_router.get("/")
def get_staff():
    return f"Hello world"


@staff_router.get("/staff")
def get_staff_rout(director: models.StaffSearch):
    director = get_staff(director)
    return director


@staff_router.post("/staff")
def create_staff(director: models.Staff):
    new_id = new_staff(director)
    return f"{{code: 201, id: {new_id}}}"

