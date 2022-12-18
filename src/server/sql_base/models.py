from typing import Optional
from pydantic import BaseModel


class BaseModelModify(BaseModel):
    id: Optional[int]


class Staff(BaseModelModify):
    user_id: Optional[int] = None
    position_id: int
    team_id: int
    surname: str
    name: str
    date_birth: str
    deleted: bool = False


class StaffSearchOptional(BaseModelModify):
    user_id: Optional[int]
    position_id: Optional[int]
    team_id: Optional[int]
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


class Viewers(BaseModelModify):
    name: str
    user_id: Optional[int] = None


class Channels(BaseModelModify):
    title: str
    abbreviated_title: str


class Shows(BaseModelModify):
    tv_channel_id: int
    topic_id: int
    team_staff_id: int
    equip_set_id: int
    schedule_id: Optional[int] = None
    venue: str
    title: str


class SchedulesID(BaseModelModify):
    tv_channel_id: int
    note: str


class ScheduleOfShows(BaseModelModify):
    schedule_id: int
    show_id: int
    time_id: int


class ShowsTime(BaseModelModify):
    time: str


class Equipments(BaseModelModify):
    equipment: str
    equip_set_id: int


class EquipmentNameSets(BaseModelModify):
    name: str


class EquipmentSets(BaseModelModify):
    equip_id: int
    name_set_id: int


class StaffTeams(BaseModelModify):
    name: str
