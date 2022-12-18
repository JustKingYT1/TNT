from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Shows
from typing import Any


def new_show(show: Shows) -> int | dict:
    show_id = base_worker.execute(
        query="INSERT INTO tv_channel_shows(tv_channel_id, topic_id, team_staff_id, equipment_set_id, schedule_id, venue, title)" 
              "VALUES (?, ?, ?, ?, ?, ?, ?)"
              "RETURNING id",
        args=(show.tv_channel_id, show.topic_id, show.team_staff_id, show.equip_set_id, show.schedule_id, show.venue,
              show.title))

    if type(show_id) != dict:
        return show_id[0]

    return show_id


def get_show(show_id: int) -> Shows | dict:
    res = base_worker.execute(
        query="SELECT tv_channel_id, topic_id, team_staff_id, equipment_set_id, schedule_id, venue, title FROM  tv_channel_shows WHERE id=?",
        args=(show_id,), )
    return None if not res else Shows(
        id=res[0],
        tv_channel_id=res[1],
        topic_id=res[2],
        team_staff_id=res[3],
        equip_set_id=[4],
        schedule_id=res[5],
        venue=res[6],
        title=res[7])


def get_all_shows() -> list[Shows] | dict:
    shows_list = base_worker.execute(
        query="SELECT id, tv_channel_id, topic_id, team_staff_id, equipment_set_id, schedule_id, venue, title FROM tv_channel_shows",
        many=True)

    res = []

    if shows_list:
        for show in shows_list:
            res.append(Shows(
                id=show[0],
                tv_channel_id=show[1],
                topic_id=show[2],
                team_staff_id=show[3],
                equip_set_id=[4],
                schedule_id=show[5],
                venue=show[6],
                title=show[7]))

    return res


def upd_show(show_id: int, new_data: Shows) -> tuple[Any, Any] | dict:
    return base_worker.execute(query="UPDATE schedule_of_shows SET (schedule_id) = (?) WHERE show_id=?",
                               args=(new_data.schedule_id, show_id,)), \
           base_worker.execute(query='UPDATE tv_channel_shows '
                                     'SET (schedule_id, tv_channel_id, team_staff_id, topic_id, equipment_set_id, venue, title) = (?, ?, ?, ?, ?, ?, ?) '
                                     'WHERE id=(?)',
                               args=(new_data.schedule_id, new_data.tv_channel_id, new_data.team_staff_id,
                                     new_data.topic_id, new_data.equip_set_id, new_data.venue, new_data.title, show_id))


def del_show(show_id: int) -> tuple[Any, Any] | dict:
    return base_worker.execute(query="DELETE FROM schedule_of_shows WHERE show_id=?",
                               args=(show_id,)), \
           base_worker.execute(query="DELETE FROM tv_channel_shows WHERE id=(?)",
                               args=(show_id,))
