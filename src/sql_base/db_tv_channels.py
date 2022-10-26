import sqlite3 as sql
from src import loader
import os


def check_base(file_path: str) -> bool:
    return os.path.exists(file_path)


def create_base(file_path: str, parameter) -> None:
    connection = sql.connect(file_path)
    cursor = connection.cursor()
    for table in loader.parameter:
        try:
            cursor.execute(table)
            connection.commit()
        except sql.Error as ex:
            print(ex)
            continue
