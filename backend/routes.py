from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from backend.models import Usuario, DatosRed
from backend.app import db
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    email = request.form['email']
    contraseña = request.form['contraseña']

    if not nombre or not email or not contraseña:
        flash('Todos los campos son obligatorios')
        return redirect(url_for('index'))

    nuevo_usuario = Usuario(nombre=nombre, email=email, contraseña=generate_password_hash(contraseña))
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario creado exitosamente')
    except Exception as e:
        db.session.rollback()  # Deshacer la sesión en caso de error
        flash('Error al crear el usuario: {}'.format(str(e)))

    return redirect(url_for('index'))

@main.route('/dashboard')
def dashboard():
    datos_red = DatosRed.query.all()
    return render_template('dashboard.html', datos_red=datos_red)

@main.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        mensaje = request.form.get('mensaje')
        flash('Mensaje enviado: {}'.format(mensaje))
        return redirect(url_for('contacto'))
    return render_template('contacto.html')

# Nuevo endpoint para cargas de servidores
@main.route('/cargas_servidores')
def cargas_servidores():
    cargas = {
        "servidor1": [10, 20, 30, 40],
        "servidor2": [15, 25, 35, 45],
    }
    return jsonify(cargas)

# Nuevo endpoint para latencia de red
@main.route('/latencia_red')
def latencia_red():
    latencia = {
        "actual": 200,
        "promedio": 180,
        "prediccion": 220,
    }
    return jsonify(latencia)

# Nuevo endpoint para gestión de congestión
@main.route('/gestion_congestion')
def gestion_congestion():
    congestiones = [
        {"tiempo": "10:00", "nivel": "alto"},
        {"tiempo": "11:00", "nivel": "bajo"},
    ]
    return jsonify(congestiones)

# Agregar más endpoints según sea necesario




