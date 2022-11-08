import fastapi
from ..sql_base.models import Editors
from ..resolvers import new_editor


editor_router = fastapi.APIRouter()


@editor_router.post("/director")
def create_director(editor: Editors):
    new_id = new_editor(editor)
    return f"{{code: 201, id: {new_id}}}"


@editor_router.get("/directors")
def get_editors():
    return f"all directors: "
