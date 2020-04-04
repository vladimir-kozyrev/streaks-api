from fastapi.testclient import TestClient
from main import app
from .test_users import test_user_email

client = TestClient(app)

test_habit_name = "Study Python for 30 minutes"
test_habit_streak = 0

def test_create_habit():
    user = client.get(f"/v1/user/{test_user_email}")
    user_id = user.json()["id"]
    response = client.post(
        "/v1/habits",
        json={
            "name": test_habit_name,
            "streak": test_habit_streak,
            "user_id": user_id
        }
    )
    assert response.status_code == 200
