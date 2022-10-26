import sqlite3 as sql
from loader import LoaderToJson as json

connection = sql.connect('tv_channels.db')
tables = json.load("scripts.json")["tables"].split(";")
data = json.load("scripts.json")["data"].split(";")
with connection:
    try:
        cursor = connection.cursor()
        for table in tables:
            try:
                cursor.execute(table)
            except sql.Error as ex:
                print(ex)
                continue
        for one_data in data:
            try:
                cursor.execute(one_data)
            except sql.Error as ex:
                print(ex)
                continue
        cursor.execute('')
        connection.commit()
    except sql.Error as ex:
        print(ex)
        connection.rollback()
    # finally:
    #     connection.close()
