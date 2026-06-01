from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User
from app.routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RoutineOS API",
)

app.include_router(users_router)

@app.get("/")
def read_root():
    return {
        "message":"RoutineOS API Running"
    }