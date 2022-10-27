import src.sql_base.settings as set
from sql_base import check_base, create_base
import loader

tables = loader.LoaderToJson.load("../sql/scripts.json")["tables"].split(";")
data = loader.LoaderToJson.load("../sql/scripts.json")["data"].split(";")


if __name__ == "__main__":
    if not check_base(set.BASE_PATH):
        create_base(set.BASE_PATH, tables)

