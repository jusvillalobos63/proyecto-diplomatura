import pytest
from app import app as flask_app # Renombrar para evitar conflictos

@pytest.fixture
def client():
    """Configura un cliente de prueba para la aplicación Flask."""
    with flask_app.test_client() as client:
        yield client

def test_home(client):
    """Prueba que la ruta principal '/' funcione y devuelva el mensaje."""
    rv = client.get('/')
    assert rv.status_code == 200
    # --- LÍNEA CORREGIDA (AHORA SÍ) ---
    # Agregamos la tilde a "aplicación" en la cadena de búsqueda.
    assert "aplicación base del Proyecto 1" in rv.data.decode('utf-8')

def test_health_check(client):
    """Prueba que la ruta '/health' devuelva un JSON con estado 'ok'."""
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.json == {"status": "ok"}

def test_metrics(client):
    """Prueba que la ruta '/metrics' (de Prometheus) exista."""
    rv = client.get('/metrics')
    assert rv.status_code == 200
    # Solo verificamos que exista y devuelva texto plano
    assert rv.content_type.startswith("text/plain")
