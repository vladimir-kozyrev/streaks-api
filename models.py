from pydantic import BaseModel

class Habit(BaseModel):
    id: int
    name: str
    streak: int = 0
