from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.services.auth_service import hash_password

router = APIRouter()


@router.post("/users/")
def create_user(user: UserCreate):
    db: Session = SessionLocal()

    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return {
        "id": db_user.id,
        "name": db_user.name,
        "email": db_user.email
    }

@router.get("/users")
def read_users():
    db: Session = SessionLocal()

    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        for user in users
    ]