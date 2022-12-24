from server.sql_base.models import User
from server.sql_base.db_tv_channels import base_worker


def register_staff(user: User, staff_id: int) -> int | dict:
    id_staff = base_worker.execute(query="""INSERT INTO users_staff(staff_id, login, password)
                                           VALUES (?, ?, ?) 
                                           RETURNING staff_id""",
                                   args=(staff_id, user.login, user.password))[0]
    return base_worker.execute(
        query="""UPDATE staff
                  SET user_id=?
                  WHERE id=?
                  RETURNING id""",
        args=(id_staff, staff_id),
        many=False)[0]


def check_login_staff(user: User) -> int | dict:
    return base_worker.execute(query="""SELECT S.position_id FROM staff S
                                        INNER JOIN users_staff U ON S.user_id = U.staff_id
                                        WHERE U.login = ? AND U.password = ?""",
                               args=(user.login, user.password),
                               many=False)


def del_user_staff(user_id: int) -> None | dict:
    return base_worker.execute(query="""DELETE FROM users_staff WHERE id=?""", args=(user_id,))


def upd_user_staff(user_id: int, new_data: User) -> None | dict:
    return base_worker.execute(query="""UPDATE users_staff SET login=?, password=? WHERE id=?""",
                               args=(new_data.login, new_data.password, user_id))


def user_get_staff(user_id: int) -> User | dict:
    user = base_worker.execute(query="SELECT id, staff_id, login, password FROM users_staff WHERE id=?", args=(user_id,))
    return User(
        id=user[0],
        staff_id=[1],
        login=user[2],
        password=user[3])


def all_user_get_staff() -> list[User] | dict:
    user_list = base_worker.execute(query="SELECT id, staff_id, login, password FROM users_staff", many=True)

    res = []

    if user_list:
        for user in user_list:
            res.append(User(
                id=user[0],
                staff_id=user[1],
                login=user[2],
                password=user[3]))

    return res
