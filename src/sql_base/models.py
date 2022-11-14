from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Directors(BaseModel):
    position_id: Optional[int] = 1
    surname: str
    named: str
    date_birth: datetime


class Editors(BaseModel):
    position_id: Optional[int] = 2
    surname: str
    named: str
    date_birth: datetime
