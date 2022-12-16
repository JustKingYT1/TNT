from server.sql_base.models import User, UserSearch
from server.sql_base.db_tv_channels import base_worker


def register_viewer(user: User, viewer_id: int) -> int:
    return base_worker.execute(
        query="""UPDATE viewers
                  SET user_id=?
                  WHERE id=?
                  RETURNING id""",
        args=(base_worker.execute(query="""INSERT INTO users_viewers(viewer_id, login, password)
                                           VALUES (?, ?, ?) 
                                           RETURNING id""",
                                  args=(viewer_id, user.login, user.password))[0], viewer_id),
        many=False)[0]


def check_login_viewer(user: User) -> int:
    return base_worker.execute(query="""SELECT V.id FROM viewers V
                                        INNER JOIN users_viewers U ON V.user_id = U.id
                                        WHERE U.login = ? AND U.password = ?""",
                               args=(user.login, user.password),
                               many=False)


def del_user_viewer(user_id: int) -> None | dict:
    return base_worker.execute(query="""DELETE FROM users_viewers WHERE id=?""", args=(user_id,))


def upd_user_viewer(user_id: int, new_data: User) -> None | dict:
    return base_worker.execute(query="""UPDATE users_viewers SET login=?, password=? WHERE id=?""",
                               args=(new_data.login, new_data.password, user_id))


def user_get_viewer(user_id: int) -> User | dict:
    user = base_worker.execute(query="SELECT id, viewer_id, login, password FROM users_viewers WHERE id=?", args=(user_id,))
    return User(
        id=user[0],
        staff_id=[1],
        login=user[2],
        password=user[3])


def all_user_get_viewer() -> list[User] | dict:
    user_list = base_worker.execute(query="SELECT id, viewer_id, login, password FROM users_viewers", many=True)

    res = []

    if user_list:
        for user in user_list:
            res.append(User(
                id=user[0],
                staff_id=user[1],
                login=user[2],
                password=user[3]))

    return res
