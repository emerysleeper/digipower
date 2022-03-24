import os

if os.environ.get('IS_CONTAINER', False):
    from . import router
else:
    import router

from fastapi import FastAPI
app = FastAPI()


app.include_router(router.router)

