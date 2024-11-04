import time
import requests
from app import db, Latencia
import matplotlib.pyplot as plt
import numpy as np

# Listas para almacenar latencias y tiempos
latencias = []
tiempos = []

def monitorear_servidor(url):
    while True:
        try:
            inicio = time.time()
            response = requests.get(url)
            tiempo_respuesta = (time.time() - inicio) * 1000  # Convertir a ms

            # Almacenar datos en la base de datos
            latencia = Latencia(servidor=url, tiempo_respuesta=tiempo_respuesta)
            db.session.add(latencia)
            db.session.commit()

            # Agregar latencia y tiempo a las listas para visualización
            latencias.append(tiempo_respuesta)
            tiempos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            print(f'[{tiempos[-1]}] {url} - Latencia: {tiempo_respuesta:.2f} ms')

            # Visualización de latencias en tiempo real
            visualizar_latencia(tiempos, latencias)

            time.sleep(60)  # Monitorear cada minuto
        except Exception as e:
            print(f'Error al monitorear {url}: {e}')

def visualizar_latencia(tiempos, latencias):
    plt.clf()  # Limpiar la figura actual
    plt.plot(tiempos[-10:], latencias[-10:], marker='o', color='b', label='Latencia (ms)')
    plt.title('Monitoreo de Latencia en Tiempo Real')
    plt.xlabel('Tiempo')
    plt.ylabel('Latencia (ms)')
    plt.xticks(rotation=45)
    plt.ylim(0, max(latencias) + 10 if latencias else 10)  # Ajustar el límite del eje y
    plt.legend()
    plt.pause(0.01)  # Pausar para permitir que se actualice el gráfico

if __name__ == "__main__":
    url_servidor = 'http://example.com'  # Cambia esto a la URL que deseas monitorear
    plt.ion()  # Activar modo interactivo de matplotlib
    monitorear_servidor(url_servidor)

