from ..sql_base import base_worker
from ..sql_base import models


def new_editor(editor: models.Editors) -> int:
    new_id = base_worker.insert_data("INSERT INTO staff(position_id, named, surname, date_birth)"
                                     "VALUES (2, ?, ?, ?)"
                                     "RETURNING id",
                                     (editor.named, editor.surname, editor.date_birth))
    return new_id
