from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Staff, StaffSearch, GetStaff


def new_staff(staff: Staff) -> int | dict:
    res = base_worker.execute(query="INSERT INTO staff(position_id, user_id, named, surname, date_birth, deleted)"
                              "VALUES (?, ?, ?, ?, ?, ?)"
                              "RETURNING id",
                              args=(staff.position_id, staff.user_id, staff.named, staff.surname, staff.date_birth, staff.deleted))
    if type(res) != dict:
        return res[0]

    return res


def get_staff(staff_id: int) -> Staff:
    res = base_worker.execute(query="SELECT id, position_id, user_id, named, surname, date_birth, deleted FROM staff WHERE id=?",
                              args=(staff_id,),
                              many=False)
    return None if not res else Staff(
        id=res[0],
        position_id=res[1],
        user_id=res[2],
        named=res[3],
        surname=res[4],
        date_birth=res[5],
        deleted=res[6]
    )


def get_all_staff() -> list[Staff] | dict:
    staff_list = base_worker.execute(query="SELECT * FROM staff", many=True)
    print(staff_list)

    res = []

    if staff_list:
        for user in staff_list:
            res.append(Staff(
                id=user[0],
                position_id=user[1],
                user_id=user[2],
                named=user[3],
                surname=user[4],
                date_birth=user[5],
                deleted=user[6]

            ))
            for elem in user:
                print(elem)

    return res


def get_staff_optional(staff: StaffSearch) -> list[Staff] | dict:
    first_row = True
    query = "SELECT id, position_id, user_id, named, surname, date_birth, deleted FROM staff "
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
                named=user[3],
                surname=user[4],
                date_birth=user[5],
                deleted=user[6]
            ))
    return res


def upd_staff(staff_id: int, new_data: Staff) -> None:
    return base_worker.execute(query='UPDATE staff '
                                     'SET (position_id, named, surname, date_birth, deleted) = (?, ?, ?, ?, ?) '
                                     'WHERE id=(?)',
                               args=(new_data.position_id, new_data.named, new_data.surname,
                                     new_data.date_birth, new_data.deleted, staff_id))


def del_staff(staff_id: int) -> None:
    return base_worker.execute(query="DELETE FROM staff WHERE id=(?)",
                               args=(staff_id,))
