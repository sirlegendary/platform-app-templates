from app.app import app


def test_index_returns_200():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
