import fastapi
from server.sql_base.models import Viewers
from server.resolvers.viewers import get_viewer, get_all_viewers, del_viewer, new_viewer, upd_viewer
from typing import Any

viewers_router = fastapi.APIRouter(prefix='/viewers', tags=['Viewers'])


@viewers_router.get("/")
def start_page():
    return f"Hello new user!"


@viewers_router.get("/get/{viewer_id}/", response_model=Viewers | dict)
def get_viewer_rout(viewer_id: int) -> Viewers | dict:
    return get_viewer(viewer_id)


@viewers_router.get("/get/")
def get_viewers() -> list[Viewers] | dict:
    return get_all_viewers()


@viewers_router.post("/create/", response_model=int | dict)
def create_viewer(viewer: Viewers) -> int | dict:
    return new_viewer(viewer)


@viewers_router.put("/update/{viewer_id}/", response_model=None | dict)
def update_viewer(viewer_id: int, new_data: Viewers) -> None | dict:
    return upd_viewer(viewer_id, new_data)


@viewers_router.delete("/delete/{viewer_id}/", response_model=tuple[Any, Any] | dict)
def delete_viewer(viewer_id) -> tuple[Any, Any] | dict:
    return del_viewer(viewer_id)
