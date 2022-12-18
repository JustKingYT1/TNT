from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import SchedulesID, ScheduleOfShows
from typing import Any


def new_show_in_schedule(show: ScheduleOfShows) -> int | dict:
    res = base_worker.execute(query="INSERT INTO schedule_of_shows(schedule_id, show_id, time_id) VALUES (?, ?, ?) RETURNING schedule_id",
                              args=(show.schedule_id, show.show_id, show.time_id))
    return res


def new_schedule_id(schedule: SchedulesID) -> int | dict:
    res = base_worker.execute(query="INSERT INTO schedule_of_shows_id(tv_channel_id, note)"
                                    "VALUES (?, ?)"
                                    "RETURNING id",
                              args=(schedule.tv_channel_id, schedule.note,))
    if type(res) != dict:
        return res[0]

    return res


def get_schedule_id(schedule_id: int) -> SchedulesID | dict:
    res = base_worker.execute(
        query="SELECT id, tv_channel_id, note FROM schedule_of_shows_id WHERE id=?",
        args=(schedule_id,),)
    return None if not res else SchedulesID(
        id=res[0],
        tv_channel_id=res[1],
        note=res[2])


def get_all_schedules_id() -> list[SchedulesID] | dict:
    schedules_id_list = base_worker.execute(
        query="SELECT id, tv_channel_id, note FROM schedule_of_shows_id", many=True)

    res = []

    if schedules_id_list:
        for schedules_id in schedules_id_list:
            res.append(SchedulesID(
                id=schedules_id[0],
                tv_channel_id=schedules_id[1],
                note=schedules_id[2]))

    return res


def upd_schedule_id(schedule_id: int, new_data: SchedulesID) -> None | dict:
    return base_worker.execute(query='UPDATE schedule_of_shows_id '
                                     'SET (tv_channel_id, note) = (?, ?) '
                                     'WHERE id=(?)',
                               args=(new_data.tv_channel_id, new_data.note, schedule_id))


def del_schedule_id(schedule_id: int) -> tuple[Any, Any] | dict:
    return base_worker.execute(query="DELETE FROM schedule_of_shows WHERE schedule_id=?",
                               args=(schedule_id,)), \
           base_worker.execute(query="DELETE FROM schedule_of_shows_id WHERE id=(?)",
                               args=(schedule_id,), )


def get_schedule(schedule_id: int) -> ScheduleOfShows | dict:
    res = base_worker.execute(
        query="SELECT schedule_id, show_id, time_id FROM schedule_of_shows WHERE schedule_id=?",
        args=(schedule_id,),
        many=False)
    return None if not res else ScheduleOfShows(
        schedule_id=res[1],
        show_id=res[2],
        time_id=res[3])


def get_all_schedules() -> list[ScheduleOfShows] | dict:
    schedules_list = base_worker.execute(
        query="SELECT schedule_id, show_id, time_id FROM schedule_of_shows", many=True)

    res = []

    if schedules_list:
        for schedule in schedules_list:
            res.append(ScheduleOfShows(
                schedule_id=schedule[0],
                show_id=schedule[1],
                time_id=schedule[2]))

    return res
