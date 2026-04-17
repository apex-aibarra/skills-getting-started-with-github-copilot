from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI"}


def test_read_item_without_query():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}


def test_read_item_with_query():
    response = client.get("/items/42?q=example")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "example"}
