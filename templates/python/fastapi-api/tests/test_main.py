from fastapi.testclient import TestClient

from app.main import app


def test_root_returns_ok():
    client = TestClient(app)
    res = client.get("/")
    assert res.status_code == 200


def test_health_returns_healthy():
    client = TestClient(app)
    res = client.get("/health")
    assert res.status_code == 200
