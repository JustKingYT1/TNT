from typing import Optional
from pydantic import BaseModel


class BaseModelModify(BaseModel):
    id: Optional[int]


class Staff(BaseModelModify):
    user_id: Optional[int]
    position_id: int
    surname: str
    named: str
    date_birth: str
    deleted: str


class StaffSearch(BaseModelModify):
    user_id: Optional[int]
    position_id: Optional[int]
    surname: Optional[str]
    named: Optional[str]
    date_birth: Optional[str]
    deleted: Optional[str]


class User(BaseModelModify):
    login: str
    password: str
