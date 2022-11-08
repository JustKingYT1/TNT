from ..sql_base import base_worker
from ..sql_base import models


def new_director(director: models.Director) -> int:
    new_id = base_worker.insert_data("INSERT INTO staff(position_id, named, surname, date_birth)"
                                     "VALUES (1, ?, ?, ?)"
                                     "RETURNING id",
                                     (director.named, director.surname, director.date_birth))
    return new_id
