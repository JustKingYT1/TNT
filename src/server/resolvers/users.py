from server.sql_base.models import User, UserSearch
from server.sql_base.db_tv_channels import base_worker


def create_user(user: User, staff_id: int) -> int:
    query = """INSERT INTO users(login, password)
                VALUES (?, ?) 
                RETURNING id"""
    res = base_worker.execute(
        query="""UPDATE staff
                  SET user_id=?
                  WHERE id=?""",
        args=(base_worker.execute(query=query, args=(user.login, user.password)), staff_id))
    print(res)
    return res


def check_login_1(user: User) -> int:
    query = """SELECT position_id FROM staff S
                INNER JOIN users U ON S.user_id = U.id
                WHERE U.login = ? AND U.password = ?"""
    return base_worker.execute(query=query, args=(user.login, user.password), many=False)
