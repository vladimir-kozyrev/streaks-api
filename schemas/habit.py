from typing import List
from pydantic import BaseModel

class HabitBase(BaseModel):
    name: str


class HabitCreateSchema(HabitBase):
    pass


class HabitSchema(HabitBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
