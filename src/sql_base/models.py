from typing import Optional
from pydantic import BaseModel


class Staff(BaseModel):
    id: Optional[int]
    user_id: int
    position_id: int
    surname: str
    named: str
    date_birth: str


class StaffSearch(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    position_id: Optional[int]
    surname: Optional[str]
    named: Optional[str]
    date_birth: Optional[str]


class User(BaseModel):
    login: str
    password: str
