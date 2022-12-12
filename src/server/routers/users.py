from fastapi import APIRouter
from sql_base.models import User
from server.resolvers import check_login_1

user_router = APIRouter()


@user_router.get('/')
def not_login():
    return {"Message": "Login in system"}


@user_router.get('/login')
def check_login(user: User):
    position_id = check_login_1(user)
    if position_id:
        return {"code": 200, "message": "Login correct", "position_id": position_id}
    else:
        return {"code": 401, "message": "Login incorrect, try again", "position_id": None}
