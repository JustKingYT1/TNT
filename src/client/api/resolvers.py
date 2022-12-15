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

def check_login(login: str, password: str):
    data = f'{{ "login": "{login}", "password": "{password}" }}'
    r = requests.get(url='http://127.0.0.1:8000/users/login', data=data)
    answer = r.json()
    code = answer["code"]
    message = answer["message"]

    if code != 200:
        print(f"Server error: {message}")
    if answer["position_id"] is not None:
        return answer["position_id"][0]
