import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

# Cargar datos desde un archivo CSV
def cargar_datos(ruta_archivo):
    """Carga datos de tráfico desde un archivo CSV."""
    try:
        data = pd.read_csv(ruta_archivo)
        print(f"Datos cargados con éxito desde {ruta_archivo}.")
        return data
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

# Analizar latencia
def analizar_latencia(data):
    """Analiza la latencia en función del tiempo y la carga."""
    plt.figure(figsize=(12, 6))
    
    # Gráfico de líneas para latencia
    plt.subplot(2, 1, 1)
    plt.plot(data['tiempo'], data['latencia'], label='Latencia', color='blue')
    plt.title('Análisis de Latencia')
    plt.xlabel('Tiempo')
    plt.ylabel('Latencia (ms)')
    plt.legend()

    # Predicción de latencia
    modelo = LinearRegression()
    X = data[['tiempo']]  # Requiere que 'tiempo' esté en formato numérico
    y = data['latencia']
    modelo.fit(X, y)
    data['latencia_predicha'] = modelo.predict(X)

    # Gráfico de latencia predicha
    plt.subplot(2, 1, 2)
    plt.plot(data['tiempo'], data['latencia_predicha'], label='Latencia Predicha', color='orange', linestyle='--')
    plt.title('Predicción de Latencia')
    plt.xlabel('Tiempo')
    plt.ylabel('Latencia (ms)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Analizar tráfico
def analizar_trafico(data):
    """Analiza el tráfico de red y genera visualizaciones."""
    plt.figure(figsize=(12, 6))

    # Gráfico de áreas apiladas para el tráfico
    sns.lineplot(data=data, x='tiempo', y='trafico', label='Tráfico', color='green')
    plt.fill_between(data['tiempo'], data['trafico'], color='green', alpha=0.3)

    plt.title('Análisis de Tráfico de Red')
    plt.xlabel('Tiempo')
    plt.ylabel('Tráfico (bytes/s)')
    plt.legend()
    plt.show()

# Función principal
def main():
    ruta_archivo = 'ruta/a/tu/archivo_de_trafico.csv'  # Cambia esto a la ruta real
    data = cargar_datos(ruta_archivo)
    
    if data is not None:
        analizar_latencia(data)
        analizar_trafico(data)

if __name__ == "__main__":
    main()
