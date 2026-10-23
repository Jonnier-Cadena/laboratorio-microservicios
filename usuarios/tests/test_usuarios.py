from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health():
    response = client.get("/usuarios/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_listar_usuarios():
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
