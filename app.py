from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

"""
Proyecto Diplomatura - Aplicación Base

Integrantes:
- Leonel Galetto
- Justo Suarez Villalobos

Resumen:
Aplicación Flask con rutas básicas, healthcheck y métricas para Prometheus.
Incluye dockerización, CI/CD con GitHub Actions y monitoreo con Grafana.
"""

# Métricas
home_visits_counter = Counter(
    "home_visits",
    "Numero de visitas a la pagina principal"
)

app = Flask(__name__)


@app.route("/")
def home():
    """Ruta principal: Devuelve saludo y actualiza métricas."""
    home_visits_counter.inc()
    return "¡Hola! Esta es la aplicación base del Proyecto 1."


@app.route("/health")
def health_check():
    """Health Check: Verificación de estado del servicio."""
    return "OK", 200


@app.route("/metrics")
def metrics():
    """Endpoint de métricas para Prometheus."""
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)

