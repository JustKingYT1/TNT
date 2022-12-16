import fastapi
from server.sql_base.models import Channels
from server.resolvers.tv_channels import get_channel, new_channel, del_channel, upd_channel, get_all_channels


channel_router = fastapi.APIRouter(prefix='/channels', tags=['TVChannels'])


@channel_router.get("/")
def start_page():
    return f"Hello new user!"


@channel_router.get("/get/{channel_id}/", response_model=Channels | dict)
def get_staff_rout(channel_id: int) -> Channels | dict:
    return get_channel(channel_id)


@channel_router.get("/get/")
def get_staff_all() -> list[Channels] | dict:
    return get_all_channels()


@channel_router.post("/create/", response_model=int | dict)
def create_staff(channel: Channels) -> int | dict:
    return new_channel(channel)


@channel_router.put("/update/{channel_id}/", response_model=None | dict)
def update_staff(channel_id: int, new_data: Channels) -> None | dict:
    return upd_channel(channel_id, new_data)


@channel_router.delete("/delete/{channel_id}/", response_model=None | dict)
def delete_staff(channel_id) -> None | dict:
    return del_channel(channel_id)
