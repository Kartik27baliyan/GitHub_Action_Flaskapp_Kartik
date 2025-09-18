import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to GitHub Actions Flask App" in response.data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_greet_endpoint(client):
    response = client.get('/api/greet/Kartik')
    assert response.status_code == 200
    assert b"Hello, Kartik" in response.data
