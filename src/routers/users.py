from fastapi import APIRouter
from sql_base.models import User
from resolvers import check_login

user_router = APIRouter()


@user_router.get('/')
def not_login():
    return {"Message": "Login in system"}


@user_router.get('/login')
def check_login(user: User):
    staff_id = check_login(user)
    if staff_id:
        return {"code": 200, "message": "Login correct", "staff_id": staff_id}
    else:
        return {"code": 401, "message": "Login incorrect, try again", "staff_id": None}
