import sqlite3
import os


class BaseWorker:

    def set_base_path(self, base_path: str):
        self.base_path = base_path

    def check_base(self) -> bool:
        return os.path.exists(self.base_path)

    def create_base(self, sql_file: str) -> None:
        connection = sqlite3.connect(self.base_path)
        cur = connection.cursor()
        with open(sql_file, 'r') as file:
            scripts = file.read()
            try:
                cur.executescript(scripts)
                connection.commit()
            except sqlite3.Error as error:
                print(error)
            finally:
                connection.close()

    def execute(self, query: str, args: tuple[str] = (), many: bool = False):
        connection = sqlite3.connect(self.base_path, isolation_level=None)
        cur = connection.cursor()
        res_ctx = cur.execute(query, args)
        if not res_ctx:
            return None
        if many:
            res = res_ctx.fetchall()
        else:
            res = res_ctx.fetchone()
        connection.commit()
        connection.close()
        return res
