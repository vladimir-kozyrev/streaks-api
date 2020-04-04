from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
test_user_name = "testuser1"
test_user_email = "test@test.com"
test_user_password = "testpassword"

def test_get_users():
    response = client.get("/v1/users")
    assert response.status_code == 200

def test_create_user():
    response = client.post(
        "/v1/users",
        json={
            "name": test_user_name,
            "email": test_user_email,
            "password": test_user_password
        }
    )
    assert response.status_code == 200

def test_update_user():
    response = client.put(
        "/v1/users",
        json={
            "name": test_user_name,
            "email": test_user_email,
            "password": test_user_password
        }
    )
    assert response.status_code == 200

def test_create_user_with_same_name():
    response = client.post(
        "/v1/users",
        json={
            "name": test_user_name,
            "email": test_user_email,
            "password": test_user_password
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "A user with that email already exists."}

def test_delete_user():
    response = client.delete(
        f"/v1/user/{test_user_email}"
    )
    assert response.status_code == 200
