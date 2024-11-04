from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

class DatosRed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carga = db.Column(db.Float, nullable=False)
    latencia = db.Column(db.Float, nullable=False)
    latencia_predicha = db.Column(db.Float, nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<DatosRed {self.id} - Carga: {self.carga}, Latencia: {self.latencia}>'


class CargaServidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carga = db.Column(db.Float, nullable=False)






