import unittest
from backend.app import app, db
from backend.models import Usuario, DatosRed

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenido a la App de Gestion de Redes', response.data)  # Cambiado a "Gestion"

    def test_dashboard(self):
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_crear_usuario(self):
        usuario = Usuario(nombre="Juan", email="juan@example.com", contraseña="123456")
        db.session.add(usuario)
        db.session.commit()
        self.assertEqual(Usuario.query.count(), 1)

    def test_crear_dato_red(self):
        dato_red = DatosRed(carga=75.5, latencia=20.3)
        db.session.add(dato_red)
        db.session.commit()
        self.assertEqual(DatosRed.query.count(), 1)

if __name__ == '__main__':
    unittest.main()

