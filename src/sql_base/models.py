from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Staff(BaseModel):
    id: Optional[int]
    position_id: Optional[int]
    surname: str
    named: str
    date_birth: str


class StaffSearch(BaseModel):
    position_id: Optional[int]
    surname: Optional[str]
    named: Optional[str]
    date_birth: Optional[str]


class User(BaseModel):
    position_id: Optional[int]
    login: str
    password: str
    reg_date: Optional[datetime]


class Subjects(BaseModel):
    id: Optional[int]
    name: str

