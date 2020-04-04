from typing import List
from pydantic import BaseModel

class HabitBase(BaseModel):
    name: str
    streak: int = 0

class HabitCreateSchema(HabitBase):
    user_id: int


class HabitSchema(HabitBase):
    id: int

    class Config:
        orm_mode = True
