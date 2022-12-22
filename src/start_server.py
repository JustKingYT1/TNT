from fastapi import FastAPI
from server.router import routs
from fastapi.responses import RedirectResponse
import uvicorn
import settings

app = FastAPI(title='tvAPI',
              version='0.1 Alpha')

[app.include_router(rout) for rout in routs]


@app.router.get('/')
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    uvicorn.run("start_server:app", reload=True, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
