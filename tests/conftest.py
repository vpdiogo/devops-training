import pytest
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture(scope="session")
def test_app():
    """Create FastAPI test application"""
    return app

@pytest.fixture(scope="session")
def client(test_app):
    """Create test client for FastAPI app"""
    return TestClient(test_app)
