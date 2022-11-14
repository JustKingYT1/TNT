import fastapi
from sql_base import models
from resolvers import new_director


director_router = fastapi.APIRouter()


@director_router.post("/")
def create_director(director: models.Directors):
    new_id = new_director(director)
    return f"{{code: 201, id: {new_id}}}"


@director_router.get("/")
def get_directors():
    return f"all directors: "
