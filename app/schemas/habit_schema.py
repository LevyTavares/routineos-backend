from pydantic import BaseModel


class HabitCreate(BaseModel):

    title: str

    frequency: str = "daily"

    completed: bool = False