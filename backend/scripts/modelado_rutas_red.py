import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import seaborn as sns

# Configuración de estilo para gráficos
sns.set(style="whitegrid")

# Función para cargar datos (puedes ajustar la fuente de datos según tu configuración)
def cargar_datos(ruta_archivo):
    data = pd.read_csv(ruta_archivo)
    return data

# Función para modelar y predecir rutas de red
def modelar_rutas(data):
    # Supongamos que tenemos columnas: 'origen', 'destino', 'latencia', 'carga', 'tiempo'
    X = data[['latencia', 'carga']]
    y = data['tiempo']
    
    modelo = LinearRegression()
    modelo.fit(X, y)
    data['tiempo_predicho'] = modelo.predict(X)

    return modelo, data

# Función para visualizar la relación entre carga y latencia
def visualizar_carga_latencia(data):
    plt.figure(figsize=(10, 5))
    plt.scatter(data['carga'], data['latencia'], alpha=0.6)
    plt.title('Relación entre Carga y Latencia')
    plt.xlabel('Carga (requests/sec)')
    plt.ylabel('Latencia (ms)')
    plt.grid(True)
    plt.show()

# Función para analizar rutas utilizando KMeans
def analizar_rutas(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    data['cluster'] = kmeans.fit_predict(data[['latencia', 'carga']])
    
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=data, x='carga', y='latencia', hue='cluster', palette='viridis', s=100)
    plt.title('Análisis de Rutas por Clúster')
    plt.xlabel('Carga (requests/sec)')
    plt.ylabel('Latencia (ms)')
    plt.legend(title='Cluster')
    plt.show()

# Función principal para ejecutar el modelado y visualizaciones
def main():
    # Cargar datos (ajustar la ruta según sea necesario)
    ruta_archivo = 'ruta/a/tu/archivo.csv'  # Cambia esto a la ruta de tu archivo CSV
    data = cargar_datos(ruta_archivo)

    # Modelar rutas
    modelo, data_modelada = modelar_rutas(data)
    
    # Visualizar resultados
    visualizar_carga_latencia(data_modelada)
    analizar_rutas(data_modelada, n_clusters=3)

    # Imprimir coeficientes del modelo
    print("Coeficientes del modelo:", modelo.coef_)
    print("Intercepto del modelo:", modelo.intercept_)

if __name__ == "__main__":
    main()
