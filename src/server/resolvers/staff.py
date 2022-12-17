from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Staff, StaffSearchOptional
from typing import Any


def new_staff(staff: Staff) -> None | dict:
    staff_id = base_worker.execute(query="INSERT INTO staff(position_id, team_id, name, surname, date_birth, deleted)"
                                         "VALUES (?, ?, ?, ?, ?, ?)"
                                         "RETURNING id, team_id",
                                   args=(staff.position_id, staff.team_id, staff.name, staff.surname, staff.date_birth,
                                         staff.deleted))

    res = base_worker.execute(query="INSERT INTO staff_teams(staff_id, team_id) VALUES (?, ?)",
                              args=(staff_id[0], staff_id[1]))

    return res


def get_staff(staff_id: int) -> Staff | dict:
    res = base_worker.execute(
        query="SELECT id, position_id, user_id, name, surname, date_birth, deleted FROM staff WHERE id=?",
        args=(staff_id,),
        many=False)
    return None if not res else Staff(
        id=res[0],
        position_id=res[1],
        user_id=res[2],
        team_id=res[3],
        name=res[4],
        surname=res[5],
        date_birth=res[6],
        deleted=res[7]
    )


def get_all_staff() -> list[Staff] | dict:
    staff_list = base_worker.execute(
        query="SELECT id, position_id, user_id, name, surname, date_birth, deleted FROM staff", many=True)

    res = []

    if staff_list:
        for staff in staff_list:
            res.append(Staff(
                id=staff[0],
                position_id=staff[1],
                user_id=staff[2],
                team_id=staff[3],
                name=staff[4],
                surname=staff[5],
                date_birth=staff[6],
                deleted=staff[7]

            ))

    return res


def get_staff_optional(staff: StaffSearchOptional) -> list[Staff] | dict:
    first_row = True
    query = "SELECT id, position_id, user_id, name, surname, date_birth, deleted FROM staff "
    for key, value in staff.__dict__.items():
        if value is not None:
            if not first_row:
                query += "AND "
            else:
                query += "WHERE "
            query += f"{key} = \"{value}\" "
            first_row = False

    staff_list = base_worker.execute(query=query, many=True)

    res = []

    if staff_list:
        for user in staff_list:
            res.append(Staff(
                id=user[0],
                position_id=user[1],
                user_id=user[2],
                team_id=user[3],
                name=user[4],
                surname=user[5],
                date_birth=user[6],
                deleted=user[7]
            ))
    return res


def upd_staff(staff_id: int, new_data: Staff) -> None | dict:
    team_id = base_worker.execute(query='UPDATE staff '
                                        'SET (position_id, team_id, name, surname, date_birth, deleted) = (?, ?, ?, ?, ?, ?) '
                                        'WHERE id=(?)'
                                        'RETURNING team_id',
                                  args=(new_data.position_id, new_data.team_id, new_data.name, new_data.surname,
                                        new_data.date_birth, new_data.deleted, staff_id))
    res = base_worker.execute(query="UPDATE staff_teams SET team_id=? WHERE staff_id=?",
                              args=(team_id[0], staff_id))

    return res


def del_staff(staff_id: int) -> tuple[Any, Any, Any] | dict:
    res1 = base_worker.execute(query="DELETE FROM staff_teams WHERE staff_id=?",
                               args=(staff_id,))
    res2 = base_worker.execute(query="DELETE FROM users_staff WHERE staff_id=?",
                               args=(staff_id,))
    res3 = base_worker.execute(query="DELETE FROM staff WHERE id=(?); ",
                               args=(staff_id,), )
    return res1, res2, res3
