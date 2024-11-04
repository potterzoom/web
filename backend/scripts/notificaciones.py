import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enviar_notificacion(destinatario, asunto, mensaje):
    """Envía una notificación por correo electrónico a un destinatario especificado.

    Args:
        destinatario (str): Dirección de correo electrónico del destinatario.
        asunto (str): Asunto del correo electrónico.
        mensaje (str): Cuerpo del mensaje del correo electrónico.
    """
    # Configura el servidor SMTP
    servidor_smtp = 'smtp.example.com'
    puerto = 587
    remitente = 'tu_correo@example.com'
    contrasena = 'tu_contrasena'

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        # Enviar el mensaje
        with smtplib.SMTP(servidor_smtp, puerto) as servidor:
            servidor.starttls()
            servidor.login(remitente, contrasena)
            servidor.send_message(msg)
        logging.info("Notificación enviada a: %s", destinatario)
    except Exception as e:
        logging.error("Error al enviar notificación: %s", e)

# Ejemplo de uso
if __name__ == "__main__":
    destinatario = "admin@example.com"
    asunto = "Alerta de Monitoreo"
    mensaje = "Se ha detectado una anomalía en los datos de tráfico."
    enviar_notificacion(destinatario, asunto, mensaje)
