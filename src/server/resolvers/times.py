from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import ShowsTime


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
    return base_worker.execute(query="DELETE FROM shows_time WHERE id=(?); DELETE FROM schedule_of_shows WHERE time_id=?",
                               args=(time_id, time_id),
                               many=True)
