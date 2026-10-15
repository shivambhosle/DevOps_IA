import json
import pytest
from app import app, APP_VERSION

@pytest.fixture
def client():
    """Create a Flask test client for automated testing."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage_status_code(client):
    """Test that homepage returns HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200

def test_homepage_success_message(client):
    """Test that expected success message and tools appear in homepage HTML."""
    response = client.get("/")
    content = response.data.decode("utf-8")
    assert "CI/CD Pipeline Successful!" in content
    assert "Jenkins" in content
    assert "Docker" in content
    assert f"v{APP_VERSION}" in content

def test_health_endpoint_status_and_json(client):
    """Test that /health returns HTTP 200 and valid JSON with healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["version"] == APP_VERSION
    assert data["service"] == "jenkins-docker-demo"
