from flask import Flask, render_template, redirect, url_for  # Importar redirect y url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  
import os

# Crear la aplicación Flask
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'templates'))

# Configurar la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear la instancia de SQLAlchemy y vincularla a la app
db = SQLAlchemy(app)

# Modelo para los datos de la red
class DatosRed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carga = db.Column(db.String(50), nullable=False)
    latencia = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)

# Ruta de prueba (Frontend)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')  # Ruta para la página de contacto
def contacto():
    return render_template('contacto.html')

# Ruta para el dashboard (Frontend)
@app.route('/dashboard')
def dashboard():
    # Consultar todos los datos de la tabla DatosRed
    datos_red = DatosRed.query.all()
    return render_template('dashboard.html', datos_red=datos_red)

# Ruta para el backend (Administradores)
@app.route('/admin')
def admin_dashboard():
    return render_template('base.html')

@app.route('/admin/manage_users')
def manage_users():
    return render_template('manage_users.html')  # Crea este archivo

@app.route('/admin/view_statistics')
def view_statistics():
    return render_template('view_statistics.html')  # Crea este archivo

@app.route('/admin/settings')
def settings():
    return render_template('settings.html')  # Crea este archivo

@app.route('/logout')
def logout():
    # Implementar lógica de cierre de sesión si es necesario
    return redirect(url_for('index'))  # Redirige a la página de inicio

# Ejecutar la app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(debug=True)
























