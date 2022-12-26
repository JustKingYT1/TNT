import fastapi
from server.sql_base.models import Channels
from server.resolvers.tv_channels import get_channel, new_channel, del_channel, upd_channel, get_all_channels


channel_router = fastapi.APIRouter(prefix='/channels', tags=['TVChannels'])


@channel_router.get("/")
def start_page():
    return f"Hello new user!"


@channel_router.get("/get/{channel_id}/", response_model=Channels | dict)
def get_channel_rout(channel_id: int) -> Channels | dict:
    return get_channel(channel_id)


@channel_router.get("/get/", response_model=list[Channels] | dict)
def get_channels_all() -> list[Channels] | dict:
    return get_all_channels()


@channel_router.post("/create/", response_model=int | dict)
def create_channel(channel: Channels) -> int | dict:
    res = new_channel(channel)
    if type(res) == int:
        return {"code": 200, "message": "Successfully", "channel_id": res}
    else:
        return {"code": 400, "message": "Error", "channel_id": None}


@channel_router.put("/update/{channel_id}/", response_model=None | dict | int)
def update_channel(channel_id: int, new_data: Channels) -> None | dict | int:
    res = upd_channel(channel_id, new_data)
    print(res)
    if type(res) == int:
        return {"code": 200, "message": "Successfully"}
    else:
        return {"code": 400, "message": "Error", "res": res}


@channel_router.delete("/delete/{channel_id}/", response_model=None | dict | int)
def delete_channel(channel_id) -> None | dict | int:
    res = del_channel(channel_id)
    if type(res) == int:
        return {"code": 200, "message": "Successfully"}
    else:
        return {"code": 400, "message": "Error", "res": res}
