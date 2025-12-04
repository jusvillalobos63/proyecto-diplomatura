# -----------------------------------------------------------------------------
# Proyecto Diplomatura
# Integrantes:
#   - Leonel Galetto
#   - Justo Suarez Villalobos
#
# Pasos Realizados en el Proyecto:
# 1. Desarrollo de la Aplicación (Fase 1):
#    - Creación de una aplicación web simple en Python utilizando el framework Flask.
#    - Implementación de rutas básicas ('/') y endpoints de salud ('/health').
#    - Implementación de un endpoint de métricas ('/metrics') para monitoreo.
#    - Desarrollo de pruebas unitarias con Pytest para asegurar la calidad del código.
#
# 2. Dockerización (Fase 2):
#    - Creación de un Dockerfile para empaquetar la aplicación y sus dependencias.
#    - Configuración de un entorno aislado y reproducible mediante contenedores.
#    - Verificación local de la construcción y ejecución de la imagen Docker.
#
# 3. Infraestructura como Código (Fase 3):
#    - Uso de Terraform para definir y aprovisionar la infraestructura en AWS.
#    - Creación automatizada de un servidor EC2 (t2.micro) y grupos de seguridad.
#    - Configuración de reglas de firewall para permitir tráfico HTTP, SSH y de monitoreo.
#    - Implementación de un script de inicio (user_data) para la instalación automática de Docker.
#
# 4. Integración Continua - CI (Fase 4):
#    - Configuración de un pipeline en GitHub Actions.
#    - Automatización de la instalación de dependencias.
#    - Ejecución automática de análisis de código estático (Linting con Flake8).
#    - Ejecución automática de pruebas unitarias (Pytest) ante cada cambio en el código.
#
# 5. Despliegue Continuo - CD (Fase 5):
#    - Extensión del pipeline para la construcción automática de imágenes Docker.
#    - Publicación de imágenes en Docker Hub.
#    - Despliegue automático en el servidor AWS mediante conexión SSH.
#    - Uso de GitHub Secrets para la gestión segura de credenciales.
#
# 6. Monitoreo y Observabilidad (Fase 6):
#    - Implementación de un stack de monitoreo con Prometheus y Grafana.
#    - Configuración de docker-compose para orquestar la aplicación y los servicios de monitoreo.
#    - Instrumentación de la aplicación para exponer métricas personalizadas (contador de visitas).
#    - Visualización de métricas en tiempo real mediante dashboards de Grafana.
# -----------------------------------------------------------------------------

from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# --- Métricas ---
# Contador para rastrear visitas a la página principal
home_visits_counter = Counter(
    'home_visits', 'Numero de visitas a la pagina principal'
)

app = Flask(__name__)


# --- Rutas ---

@app.route('/')
def home():
    """Ruta principal: Devuelve saludo y actualiza métricas."""
    home_visits_counter.inc()
    return "¡Hola! Esta es la aplicación base del Proyecto 1."


@app.route('/health')
def health_check():
    """Health Check: Verificación de estado del servicio."""
    return "OK", 200


@app.route('/metrics')
def metrics():
    """Endpoint de métricas para Prometheus."""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == '__main__':
    # Ejecución en puerto 5001
    app.run(debug=False, host='0.0.0.0', port=5001)
