from typing import List
from pydantic import BaseModel
from .habit import HabitSchema

class UserBase(BaseModel):
    name: str
    email: str


class UserCreateSchema(UserBase):
    password: str


class UserSchema(UserBase):
    id: int
    habits: List[HabitSchema] = []

    class Config:
        orm_mode = True
