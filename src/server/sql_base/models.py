from typing import Optional, NewType
from pydantic import BaseModel

null = NewType("null", None)


class BaseModelModify(BaseModel):
    id: Optional[int]


class Staff(BaseModelModify):
    user_id: Optional[int] = null
    position_id: int
    surname: str
    named: str
    date_birth: str
    deleted: bool = False


class StaffSearchOptional(BaseModelModify):
    user_id: Optional[int]
    position_id: Optional[int]
    surname: Optional[str]
    named: Optional[str]
    date_birth: Optional[str]
    deleted: Optional[bool]


class User(BaseModelModify):
    login: str
    password: str


class UserSearch(BaseModelModify):
    login: Optional[str]
    password: Optional[str]
