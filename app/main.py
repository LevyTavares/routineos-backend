from fastapi import FastAPI

from app.routers.users import router as users_router
from app.routers.auth import router as auth_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "RoutineOS API Running"}


app.include_router(users_router)
app.include_router(auth_router)