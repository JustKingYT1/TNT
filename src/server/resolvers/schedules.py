from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import ShowsTime, Schedules_id


def new_time(time: ShowsTime) -> int | dict:
    res = base_worker.execute(query="INSERT INTO shows_time(time_o_clock)"
                                    "VALUES (?)"
                                    "RETURNING id",
                              args=(time.time,))
    if type(res) != dict:
        return res[0]

    return res


def get_time(time_id: int) -> ShowsTime:
    res = base_worker.execute(
        query="SELECT id, time_o_clock FROM shows_time WHERE id=?",
        args=(time_id,),
        many=False)
    return None if not res else ShowsTime(
        id=res[0],
        time_o_clock=res[1])


def get_all_times() -> list[ShowsTime] | dict:
    times_list = base_worker.execute(
        query="SELECT id, time_o_clock FROM shows_time", many=True)

    res = []

    if times_list:
        for time in times_list:
            res.append(ShowsTime(
                id=time[0],
                time_o_clock=time[1]))

    return res


def upd_time(time_id: int, new_data: ShowsTime) -> None:
    return base_worker.execute(query='UPDATE shows_time '
                                     'SET (time_o_clock) = (?) '
                                     'WHERE id=(?)',
                               args=(new_data.time, time_id))


def del_time(time_id: int) -> None:
    return base_worker.execute(query="DELETE FROM shows_time WHERE id=(?)",
                               args=(time_id,))


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
    return base_worker.execute(query="DELETE FROM schedule_of_shows_id WHERE id=(?)",
                               args=(schedule_id,))
