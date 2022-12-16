from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import StaffTeams


def new_staff_team(staff_team: StaffTeams) -> int | dict:
    res = base_worker.execute(query="INSERT INTO team_names(name)"
                                    "VALUES (?)"
                                    "RETURNING id",
                              args=(staff_team.name,))
    if type(res) != dict:
        return res[0]

    return res


def get_staff_team(team_id: int) -> StaffTeams:
    res = base_worker.execute(
        query="SELECT id, name FROM team_names WHERE id=?",
        args=(team_id,),
        many=False)
    return None if not res else StaffTeams(
        id=res[0],
        name=res[1]
    )


def get_all_staff_teams() -> list[StaffTeams] | dict:
    teams_list = base_worker.execute(
        query="SELECT id, name FROM team_names", many=True)

    res = []

    if teams_list:
        for team in teams_list:
            res.append(StaffTeams(
                id=team[0],
                name=team[1]))

    return res


def upd_staff_team(team_id: int, new_data: StaffTeams) -> None:
    return base_worker.execute(query='UPDATE team_names '
                                     'SET (name) = (?) '
                                     'WHERE id=(?)',
                               args=(new_data.name, team_id))


def del_staff_team(team_id: int) -> None:
    return base_worker.execute(query="DELETE FROM team_names WHERE id=(?)",
                               args=(team_id,))
