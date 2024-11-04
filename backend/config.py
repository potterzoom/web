import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')  # Cambia esto por tu DB real
    SQLALCHEMY_TRACK_MODIFICATIONS = False

