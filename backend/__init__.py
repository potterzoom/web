from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Inicializa las extensiones
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuraciones de la aplicación
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///D:/mi-app-web-de-red/database/data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'supersecretkey'

    # Inicializa las extensiones con la aplicación
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos aquí
    from backend.models import (Usuario, DatosRed, CargaServidor, CongestionRed, 
                             AsignacionServidor, PerdidaPaquetes, UsoRecursos, 
                             AlertaPredictiva, RendimientoGlobal)

    # Importar rutas
    with app.app_context():
        from backend import routes

    return app












