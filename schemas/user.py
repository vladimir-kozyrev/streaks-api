from typing import List
from pydantic import BaseModel
from .habit import HabitSchema

class UserBase(BaseModel):
    name: str


class UserCreateSchema(UserBase):
    password: str


class UserSchema(UserBase):
    id: int
    items: List[HabitSchema] = []

    class Config:
        orm_mode = True
