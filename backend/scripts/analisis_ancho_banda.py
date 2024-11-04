from app import db, Latencia
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def analizar_latencia():
    # Obtener todos los datos de latencia
    datos = Latencia.query.all()
    df = pd.DataFrame([(d.servidor, d.tiempo_respuesta, d.fecha_hora) for d in datos],
                      columns=['Servidor', 'Tiempo Respuesta', 'Fecha/Hora'])
    
    # Convertir la columna de fecha a datetime y ordenarla
    df['Fecha/Hora'] = pd.to_datetime(df['Fecha/Hora'])
    df = df.sort_values(by='Fecha/Hora')

    # Análisis simple: promedio de tiempo de respuesta
    promedio = df['Tiempo Respuesta'].mean()
    print(f'Promedio de latencia: {promedio:.2f} ms')

    # Predicción de latencia
    X = np.array(range(len(df))).reshape(-1, 1)  # Eje X como números enteros
    y = df['Tiempo Respuesta'].values  # Eje Y como tiempos de respuesta
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    # Predicciones futuras
    predicciones = modelo.predict(X)

    # Visualización de datos
    plt.figure(figsize=(12, 6))
    plt.plot(df['Fecha/Hora'], df['Tiempo Respuesta'], label='Tiempo de Respuesta Real', color='blue')
    plt.plot(df['Fecha/Hora'], predicciones, label='Predicción de Latencia', linestyle='--', color='orange')
    plt.xlabel('Fecha/Hora')
    plt.ylabel('Tiempo de Respuesta (ms)')
    plt.title('Análisis de Latencia por Servidor')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('latencia_por_servidor.png')
    plt.show()

if __name__ == "__main__":
    analizar_latencia()

