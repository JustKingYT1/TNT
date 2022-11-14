import sqlite3
import os
from settings import BASE_PATH


def connect(fun):
    connection = sqlite3.connect(BASE_PATH)
    cur = connection.cursor()
    return fun


class BaseWorker:

    def set_base_path(self, base_path: str):
        self.base_path = base_path

    def check_base(self) -> bool:
        return os.path.exists(self.base_path)

    @connect
    def create_base(self, sql_file: str) -> None:
        with open(sql_file, 'r') as file:
            scripts = file.read()
            try:
                cur.executescript(scripts)
                connection.commit()
            except sqlite3.Error as error:
                print(error)
            finally:
                connection.close()

    def insert_data(self, query: str, args: tuple[str]):
        connection = sqlite3.connect(self.base_path, isolation_level=None)
        cur = connection.cursor()
        res = cur.execute(query, args).fetchone()
        connection.commit()
        connection.close()
        return res
