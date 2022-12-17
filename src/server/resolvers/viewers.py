from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Viewers
from typing import Any


def new_viewer(viewer: Viewers) -> int | dict:
    res = base_worker.execute(query="INSERT INTO viewers(name, user_id)"
                                    "VALUES (?, ?)"
                                    "RETURNING id",
                              args=(viewer.name, viewer.user_id))
    if type(res) != dict:
        return res[0]

    return res


def get_viewer(viewer_id: int) -> Viewers | dict:
    viewer = base_worker.execute(
        query="SELECT id, name, user_id FROM viewers WHERE id=?",
        args=(viewer_id,),
        many=False)
    return None if not viewer else Viewers(
        id=viewer[0],
        name=viewer[1],
        user_id=viewer[2])


def get_all_viewers() -> list[Viewers] | dict:
    viewers_list = base_worker.execute(
        query="SELECT id, name, user_id FROM viewers", many=True)

    res = []

    if viewers_list:
        for viewer in viewers_list:
            res.append(Viewers(
                id=viewer[0],
                name=viewer[1],
                user_id=viewer[2]))

    return res


def upd_viewer(viewer_id: int, new_data: Viewers) -> None | dict:
    return base_worker.execute(query='UPDATE viewers '
                                     'SET (name) = (?) '
                                     'WHERE id=(?)',
                               args=(new_data.name, viewer_id))


def del_viewer(viewer_id: int) -> tuple[Any, Any] | dict:
    return base_worker.execute(query="DELETE FROM users_viewers WHERE viewer_id=?",
                               args=(viewer_id,)), \
           base_worker.execute(query="DELETE FROM viewers WHERE id=(?)",
                               args=(viewer_id,))
