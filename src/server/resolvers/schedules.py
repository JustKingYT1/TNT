from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Schedules_id, ScheduleOfShows


def new_schedule_id(tv_channel_id: int) -> int | dict:
    res = base_worker.execute(query="INSERT INTO schedule_of_shows_id(tv_channel_id)"
                                    "VALUES (?)"
                                    "RETURNING id",
                              args=(tv_channel_id,))
    if type(res) != dict:
        return res[0]

    return res


def get_schedule_id(schedule_id: int) -> Schedules_id:
    res = base_worker.execute(
        query="SELECT id, tv_channel_id, note FROM schedule_of_shows_id WHERE id=?",
        args=(schedule_id,),
        many=False)
    return None if not res else Schedules_id(
        id=res[0],
        tv_channel_id=res[1],
        note=res[2])


def get_all_schedules_id() -> list[Schedules_id] | dict:
    schedules_id_list = base_worker.execute(
        query="SELECT id, tv_channel_id, note FROM schedule_of_shows_id", many=True)

    res = []

    if schedules_id_list:
        for schedules_id in schedules_id_list:
            res.append(Schedules_id(
                id=schedules_id[0],
                tv_channel_id=schedules_id[1],
                note=schedules_id[2]))

    return res


def upd_schedule_id(schedule_id: int, new_data: Schedules_id) -> None:
    return base_worker.execute(query='UPDATE schedule_of_shows_id '
                                     'SET (tv_channel_id, note) = (?, ?) '
                                     'WHERE id=(?)',
                               args=(new_data.tv_channel_id, new_data.note, schedule_id))


def del_schedule_id(schedule_id: int) -> None:
    return base_worker.execute(query="DELETE FROM schedule_of_shows_id WHERE id=(?); DELETE FROM schedule_of_shows WHERE schedule_id=?",
                               args=(schedule_id, schedule_id),
                               many=True)


def get_schedule(schedule_id: int) -> Schedules_id:
    res = base_worker.execute(
        query="SELECT id, tv_channel_id, note FROM schedule_of_shows_id WHERE id=?",
        args=(schedule_id,),
        many=False)
    return None if not res else Schedules_id(
        id=res[0],
        tv_channel_id=res[1],
        note=res[2])


def get_all_schedules() -> list[ScheduleOf] | dict:
    schedules_id_list = base_worker.execute(
        query="SELECT id, tv_channel_id, note FROM schedule_of_shows_id", many=True)

    res = []

    if schedules_id_list:
        for schedules_id in schedules_id_list:
            res.append(Schedules_id(
                id=schedules_id[0],
                tv_channel_id=schedules_id[1],
                note=schedules_id[2]))

    return res