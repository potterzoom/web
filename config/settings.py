# /config/settings.py

import os

class Config:
    # Configuración básica
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_aqui'
    DEBUG = True  # Cambiar a False en producción

    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones

# Puedes crear diferentes configuraciones para desarrollo y producción
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Se puede agregar un diccionario para manejar configuraciones según el entorno
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
