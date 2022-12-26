import requests



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


def data_for_table_tv_channels() -> list[tuple]:
    data = []
    row = []
    answer = requests.get(url="http://127.0.0.1:8000/channels/get/").json()
    for dict in answer:
        for key, value in dict.items():
            if key == "id":
                continue
            row.append(value)
        data.append(tuple(row))
        row.clear()

    return data


def new_channel(title: str, abbreviated_title: str) -> dict:
    data = f'{{ "title": "{title}", "abbreviated_title": "{abbreviated_title}" }}'
    answer = requests.post("http://127.0.0.1:8000/channels/create/", data=data).json()
    code = answer["code"]
    msg = answer["message"]
    if code != 200:
        return {"Error": msg, "code": code}
    return {"message": msg, "code": code, "channel_id": answer["channel_id"]}


def upd_channel(id: int, title: str, abbreviated_title: str) -> dict:
    data = f'{{ "title": "{title}", "abbreviated_title": "{abbreviated_title}" }}'
    answer = requests.put(f"http://127.0.0.1:8000/channels/update/{id}/", data=data).json()
    code = answer["code"]
    msg = answer["message"]
    if code != 200:
        return {"Error": msg, "code": code}
    return {"message": msg, "code": code}


def del_channel(id: int) -> dict:
    answer = requests.delete(f"http://127.0.0.1:8000/channels/delete/{id}/").json()
    code = answer["code"]
    msg = answer["message"]
    if code != 200:
        return {"Error": msg, "code": code}
    return {"message": msg, "code": code}
