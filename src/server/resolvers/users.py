from sql_base import models
from sql_base import base_worker


def check_login_1(user: models.User) -> int:
    query = """SELECT position_id FROM staff S
                INNER JOIN users U ON S.user_id = U.id
                WHERE U.login = ? AND U.password = ?"""
    post_id = base_worker.execute(query, (user.login, user.password), many=False)
    return post_id
