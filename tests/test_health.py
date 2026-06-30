"""Tests for health check endpoint."""

from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_returns_ok():
    """GET /health should return 200 with expected JSON body."""
    # Act
    response = client.get("/health")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "d_ocr"


def test_health_content_type():
    """GET /health should return application/json."""
    response = client.get("/health")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
