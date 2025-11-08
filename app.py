import os
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics # Lo usaremos en la Fase 6

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar el monitoreo con Prometheus (esto crea el endpoint /metrics)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    """Ruta principal que muestra un mensaje de bienvenida."""
    return "¡Hola! Esta es la aplicación base del Proyecto 1."

@app.route('/health')
def health_check():
    """Ruta de 'health check' para verificar que la app funciona."""
    return jsonify({"status": "ok"}), 200

# El endpoint /metrics es agregado automáticamente por la librería

if __name__ == '__main__':
    # Ejecutar la aplicación
    # Usamos host='0.0.0.0' para que sea accesible fuera del contenedor Docker
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
