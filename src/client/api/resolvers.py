from typing import Callable, Tuple, Any, Dict

import requests
from server.sql_base import models
import settings

server_url = f'https://{settings.SERVER_HOST}:{settings.SERVER_PORT}'


def server_available(func) -> Callable[[tuple[Any, ...], dict[str, Any]], dict[str, str] | Any]:
    def need_it(*args, **kwargs):
        try:
            requests.get(url=server_url)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            return {"error": 'Server not available'}

    return need_it


def check_login(login: str, password: str) -> int | str | None:
    data = f'{{ "login": "{login}", "password": "{password}" }}'
    r = requests.get(url='http://127.0.0.1:8000/users/staff/login/', data=data)
    answer = r.json()
    code = answer["code"]
    message = answer["message"]
    if code != 200:
        return f"Server error: {message}"
    if type(answer["position_id"][0]) == int:
        return answer["position_id"][0]
    elif type(answer["position_id"]) is None:
        return None

