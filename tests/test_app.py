import pytest
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture
def client():
    """Create test client for FastAPI app"""
    return TestClient(app)

def test_root_endpoint(client):
    """Test root endpoint returns correct response"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "DevOps Training API is running!" in data["message"]

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data

def test_echo_endpoint_success(client):
    """Test echo endpoint with valid message"""
    test_message = "Hello FastAPI!"
    response = client.post("/echo", json={"message": test_message})
    assert response.status_code == 200
    data = response.json()
    assert data["echo"] == test_message
    assert "HELLO FASTAPI!" in data["processed_message"]

def test_echo_endpoint_empty_message(client):
    """Test echo endpoint with empty message"""
    response = client.post("/echo", json={"message": ""})
    assert response.status_code == 400

def test_echo_endpoint_missing_field(client):
    """Test echo endpoint with missing message field"""
    response = client.post("/echo", json={})
    assert response.status_code == 422  # Validation error

def test_info_endpoint(client):
    """Test info endpoint"""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert data["framework"] == "FastAPI"
    assert data["python_version"] == "3.11"
