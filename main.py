from fastapi import FastAPI
from models import Habit

app = FastAPI()
habits = {}

@app.get("/habits")
def get_habits():
    return {"habits": habits}

@app.get("/habit/{_id}")
def get_habit(_id: int):
    if _id in habits:
        return habits[_id]
    return {"message": "Habit not found."}

@app.post("/habit")
def create_habit(habit: Habit):
    habits[habit.id] = {
        "name": habit.name,
        "streak": habit.streak
    }
    return habit
