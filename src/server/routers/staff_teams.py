import fastapi
from server.sql_base.models import StaffTeams
from server.resolvers.staff_teams import new_staff_team, upd_staff_team, del_staff_team, get_all_staff_teams, get_staff_team
from typing import Any

staff_teams_router = fastapi.APIRouter(prefix='/staff/teams', tags=['StaffTeams'])


@staff_teams_router.get("/")
def start_page():
    return f"Hello new user!"


@staff_teams_router.get("/get/{staff_team_id}/", response_model=StaffTeams | dict)
def get_staff_team_rout(staff_team_id: int) -> StaffTeams | dict:
    return get_staff_team(staff_team_id)


@staff_teams_router.get("/get/")
def get_staff_teams_all() -> list[StaffTeams] | dict:
    return get_all_staff_teams()


@staff_teams_router.post("/create/", response_model=int | dict)
def create_staff_team(staff_team: StaffTeams) -> int | dict:
    return new_staff_team(staff_team)


@staff_teams_router.put("/update/{staff_team_id}/", response_model=None | dict)
def update_staff_team(staff_team_id: int, new_data: StaffTeams) -> None | dict:
    return upd_staff_team(staff_team_id, new_data)


@staff_teams_router.delete("/delete/{staff_team_id}/", response_model=tuple[Any, Any] | dict)
def delete_staff_team(staff_team_id) -> None | dict:
    return del_staff_team(staff_team_id)
