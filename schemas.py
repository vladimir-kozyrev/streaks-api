from typing import List
from pydantic import BaseModel

class HabitBase(BaseModel):
    name: str


class HabitCreate(HabitBase):
    pass


class Habit(HabitBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: List[Habit] = []

    class Config:
        orm_mode = True
