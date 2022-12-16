from fastapi import APIRouter
from server.sql_base.models import User
from server.resolvers.users_viewer import check_login_viewer, register_viewer, user_get_viewer, all_user_get_viewer, upd_user_viewer, del_user_viewer

user_viewer_router = APIRouter(prefix='/users/viewers', tags=['UsersViewers'])


@user_viewer_router.get('/')
def not_login():
    return {"Message": "Login in system"}


@user_viewer_router.get('/login', response_model=dict)
def checking_login_viewer(user: User) -> dict:
    position_id = check_login_viewer(user=user)
    if position_id:
        return {"code": 200, "message": "Login correct", "position_id": position_id}
    else:
        return {"code": 401, "message": "Login incorrect, try again", "position_id": None}


@user_viewer_router.post('/register/{viewer_id}', response_model=dict)
def new_user_viewer(user: User, viewer_id: int) -> dict:
    try:
        user_id = register_viewer(user=user, viewer_id=viewer_id)
        if type(user_id) == int:
            return {"code": 200, "message": "You are register", "user_id": user_id}
    except KeyError:
        return {"code": 400, "message": "User account is already registered", "user_id": None}


@user_viewer_router.get("/get/{user_id}", response_model=User | dict)
def get_user(user_id: int) -> User | dict:
    return user_get_viewer(user_id=user_id)


@user_viewer_router.get("/get/", response_model=list[User] | dict)
def get_all_users() -> list[User] | dict:
    return all_user_get_viewer()


@user_viewer_router.put("/update/{user_id}", response_model=None | dict)
def update_user(user_id: int, new_data: User) -> None | dict:
    return upd_user_viewer(user_id=user_id, new_data=new_data)


@user_viewer_router.delete("/delete/{user_id}", response_model=None | dict)
def delete_user(user_id) -> None | dict:
    return del_user_viewer(user_id=user_id)
