from fastapi import FastAPI

#relative import because of pytest
if __name__ == 'main':
    import router
else:
    from app import router


app = FastAPI()

app.include_router(router.router)


















