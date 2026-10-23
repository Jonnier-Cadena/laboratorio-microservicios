from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health():
    response = client.get("/pedidos/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_listar_pedidos():
    response = client.get("/pedidos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
