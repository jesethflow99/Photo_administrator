from flask import Flask, render_template, request
from blueprints.user.routes import user
import os
from dotenv import load_dotenv
from blueprints.admin.routes import admin

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(admin, url_prefix="/admin")

# Clave secreta desde .env
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def login():
    return render_template("login.html")

# Obtener rutas desde el .env
galeria_dir = os.getenv("DIRECTORIO")  # Carpeta de imágenes en SSD externo
static_dir = os.path.join(os.getcwd(), "static", "imagenes")  # Carpeta en static/

# Verificar si la ruta existe y es un enlace simbólico
if os.path.exists(static_dir) or os.path.islink(static_dir):
    os.unlink(static_dir)  # Eliminar enlace simbólico existente

# Crear nuevo enlace simbólico
try:
    os.symlink(galeria_dir, static_dir)
    print(f"Enlace simbólico creado: {static_dir} -> {galeria_dir}")
except OSError as e:
    print(f"Error al crear el enlace simbólico: {e}")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
