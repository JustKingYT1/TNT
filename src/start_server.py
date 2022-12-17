from fastapi import FastAPI
from server.sql_base.db_tv_channels import base_worker
from server.router import routs
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI(title='tcAPI',
              version='0.1 Alpha')

[app.include_router(rout) for rout in routs]


@app.router.get('/')
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_worker.check_base():
        base_worker.create_base('../sql/tables.sql')
    uvicorn.run("start_server:app", reload=True, host='localhost')
