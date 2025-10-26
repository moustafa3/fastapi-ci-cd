from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_sum_ok():
    r = client.post("/sum", json={"numbers": [1, 2.5, 3]})
    assert r.status_code == 200
    assert r.json() == {"sum": 6.5}


def test_sum_requires_non_empty_list():
    # liste vide -> échec de validation Pydantic (422)
    r = client.post("/sum", json={"numbers": []})
    assert r.status_code == 422