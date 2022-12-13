from fastapi import APIRouter
from pydantic.error_wrappers import ValidationError
from server.sql_base.models import User
from server.resolvers.users import check_login_1, create_user

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/')
def not_login():
    return {"Message": "Login in system"}


@user_router.get('/login', response_model=dict)
def check_login(user: User) -> dict:
    position_id = check_login_1(user)
    if position_id:
        return {"code": 200, "message": "Login correct", "position_id": position_id}
    else:
        return {"code": 401, "message": "Login incorrect, try again", "position_id": None}


@user_router.post('/user/{staff_id}', response_model=int | dict)
def new_user(user: User, staff_id) -> int | dict:
    try:
        return create_user(user, staff_id)
    except KeyError:
        return {"code": 401, "msg": "User account is already registered"}
    except ValidationError as ex:
        return {"error": ex}
