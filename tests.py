from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
test_user_name = "testuser1"

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200

def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": test_user_name,
            "password": "testpassword"
        }
    )
    assert response.status_code == 200

def test_create_user_with_same_name():
    response = client.post(
        "/users",
        json={
            "name": test_user_name,
            "password": "testpassword"
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "A user with that name already exists."}

def test_delete_user():
    response = client.delete(
        f"/user/{test_user_name}"
    )
    assert response.status_code == 200
