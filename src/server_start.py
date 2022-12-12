from fastapi import FastAPI
from sql_base import base_worker
from server import routs
from fastapi.responses import RedirectResponse
import uvicorn

if not base_worker.check_base():
    base_worker.create_base('../sql/tables.sql')

app = FastAPI(title='tcAPI',
              version='0.1 Alpha')

[app.include_router(rout) for rout in routs]


@app.router.get('/', include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_worker.check_base():
        base_worker.create_base('../sql/tables.sql')
    uvicorn.run("server_start:app", reload=True, host='localhost')
