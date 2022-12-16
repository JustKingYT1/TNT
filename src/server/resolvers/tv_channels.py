from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Channels


def new_channel(channel: Channels) -> int | dict:
    res = base_worker.execute(query="INSERT INTO tv_channels(title, abbreviated_title)"
                                    "VALUES (?, ?)"
                                    "RETURNING id",
                              args=(channel.title, channel.abbreviated_title))
    if type(res) != dict:
        return res[0]

    return res


def get_channel(channel_id: int) -> Channels:
    res = base_worker.execute(
        query="SELECT id, title, abbreviated_title FROM tv_channels WHERE id=?",
        args=(channel_id,),
        many=False)
    return None if not res else Channels(
        id=res[0],
        title=res[1],
        abbreviated_title=res[2])


def get_all_channels() -> list[Channels] | dict:
    channels_list = base_worker.execute(
        query="SELECT id, title, abbreviated_title FROM tv_channels", many=True)

    res = []

    if channels_list:
        for channel in channels_list:
            res.append(Channels(
                id=channel[0],
                title=channel[1],
                abbreviated_title=channel[2]))

    return res


def upd_channel(channel_id: int, new_data: Channels) -> None:
    return base_worker.execute(query='UPDATE tv_channels '
                                     'SET (title, abbreviated_title) = (?, ?) '
                                     'WHERE id=(?)',
                               args=(new_data.title, new_data.abbreviated_title, channel_id))


def del_channel(channel_id: int) -> None:
    return base_worker.execute(query="DELETE FROM tv_channels WHERE id=(?)",
                               args=(channel_id,))
