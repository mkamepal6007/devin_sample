import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data


def test_api_hello(client):
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_health(client):
    response = client.get("/health")
    assert response.get_json() == {"status": "ok"}
