from fastapi import FastAPI

from app.database import Base, engine

from app.routers.users import router as users_router
from app.routers.auth import router as auth_router

from app.models.user import User
from app.models.habit import Habit
from app.routers.habits import (
    router as habits_router
)
app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "RoutineOS API Running"}


app.include_router(users_router)
app.include_router(auth_router)
app.include_router(
    habits_router
)