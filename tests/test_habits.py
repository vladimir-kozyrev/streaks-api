from fastapi.testclient import TestClient
from main import app
from .test_users import test_user_email

client = TestClient(app)

test_habit_name = "Study Python for 30 minutes"
test_habit_streak = 0
