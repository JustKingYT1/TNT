from server.sql_base.db_tv_channels import base_worker
import settings


if __name__ == '__main__':
    base_worker.create_base(f"{settings.SQL_SCRIPTS_DIR}/tables.sql")
