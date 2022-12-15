from server.sql_base.models import User, UserSearch
from server.sql_base.db_tv_channels import base_worker


def create_user(user: User, staff_id: int) -> int:
    return base_worker.execute(
        query="""UPDATE staff
                  SET user_id=?
                  WHERE id=?
                  RETURNING id""",
        args=(base_worker.execute(query="""INSERT INTO users(staff_id, login, password)
                                           VALUES (?, ?, ?) 
                                           RETURNING id""",
                                  args=(staff_id, user.login, user.password))[0], staff_id),
        many=False)[0]


def check_login(user: User) -> int:
    return base_worker.execute(query="""SELECT position_id FROM staff S
                                        INNER JOIN users U ON S.user_id = U.id
                                        WHERE U.login = ? AND U.password = ?""",
                               args=(user.login, user.password),
                               many=False)


def del_user(user_id: int) -> None | dict:
    return base_worker.execute(query="""DELETE FROM users WHERE id=?""", args=(user_id,))


def upd_user(user_id: int, new_data: User) -> None | dict:
    return base_worker.execute(query="""UPDATE users SET login=?, password=? WHERE id=?""",
                               args=(new_data.login, new_data.password, user_id))


def user_get(user_id: int) -> User | dict:
    user = base_worker.execute(query="SELECT id, staff_id, login, password FROM users WHERE id=?", args=(user_id,))
    return User(
        id=user[0],
        staff_id=[1],
        login=user[2],
        password=user[3]
    )


def all_user_get() -> list[User] | dict:
    user_list = base_worker.execute(query="SELECT id, staff_id, login, password FROM users", many=True)

    res = []

    if user_list:
        for user in user_list:
            res.append(User(
                id=user[0],
                staff_id=user[1],
                login=user[2],
                password=user[3]))

    return res
