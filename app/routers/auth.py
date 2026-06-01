from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.services.auth_service import verify_password
from app.services.dependencies import get_current_user
from app.services.jwt_service import create_access_token

router = APIRouter()


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me")
def me(current_user_email: str = Depends(get_current_user)):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.email == current_user_email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }