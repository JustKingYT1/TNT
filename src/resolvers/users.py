from sql_base import models
from sql_base import base_worker


def check_login_1(user: models.User) -> int:
    query = "SELECT staff_id FROM users WHERE login = ? AND password = ?"
    post_id = base_worker.execute(query, (user.login, user.password), many=False)
    return post_id
