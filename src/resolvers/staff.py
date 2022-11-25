from sql_base import base_worker
from sql_base import models


def new_staff(staff: models.Staff) -> int:
    new_id = base_worker.execute("INSERT INTO staff(position_id, named, surname, date_birth)"
                                 "VALUES (?, ?, ?, ?)"
                                 "RETURNING id",
                                 (staff.position_id, staff.named, staff.surname, staff.date_birth))
    return new_id


def get_staff(staff: models.StaffSearch):
    first_row = True
    query = "SELECT id, position_id, named, surname, date_birth FROM staff "
    for key, value in staff.__dict__.items():
        if value is not None:
            if not first_row:
                query += "AND "
            else:
                query += "WHERE "
            query += f"{key} = \"{value}\" "
            first_row = False
    get_id = base_worker.execute(query=query, many=True)
    return get_id
