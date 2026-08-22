from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.models.habit import Habit
from app.models.user import User
from app.schemas.habit_schema import HabitCreate
from app.services.dependencies import (
    get_current_user,
    get_db
)

router = APIRouter()


@router.post("/habits")
def create_habit(
    habit: HabitCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(
        get_current_user
    )
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_habit = Habit(
        title=habit.title,
        frequency=habit.frequency,
        completed=habit.completed,
        user_id=user.id
    )

    db.add(new_habit)

    db.commit()

    db.refresh(new_habit)

    return new_habit

@router.get("/habits")
def get_habits(
    current_user: str = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    habits = db.query(Habit).filter(
        Habit.user_id == user.id
    ).all()

    return habits