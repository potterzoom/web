# /backend/scripts/algoritmos_predictivos.py

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Función para cargar los datos desde un archivo CSV
def cargar_datos(ruta_archivo):
    """Carga los datos de un archivo CSV."""
    try:
        datos = pd.read_csv(ruta_archivo)
        return datos
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

# Función para preparar los datos para la predicción
def preparar_datos(datos):
    """Prepara los datos para el modelo de predicción."""
    datos['fecha'] = pd.to_datetime(datos['fecha'])
    datos['timestamp'] = datos['fecha'].astype(np.int64) // 10**9  # Convertir a timestamp
    X = datos[['timestamp']]
    
    # Asegurarse de que la columna 'valor' sea numérica
    datos['valor'] = pd.to_numeric(datos['valor'], errors='coerce')
    y = datos['valor']
    
    return X, y

# Función para entrenar el modelo
def entrenar_modelo(X, y):
    """Entrena el modelo de regresión lineal."""
    modelo = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo.fit(X_train, y_train)
    predicciones = modelo.predict(X_test)
    error = mean_squared_error(y_test, predicciones)
    print(f"Error cuadrático medio: {error:.2f}")
    return modelo

# Función para guardar el modelo
def guardar_modelo(modelo, ruta):
    """Guarda el modelo entrenado en un archivo."""
    try:
        joblib.dump(modelo, ruta)
        print(f"Modelo guardado en: {ruta}")
    except Exception as e:
        print(f"Error al guardar el modelo: {e}")

# Función para cargar el modelo
def cargar_modelo(ruta):
    """Carga un modelo previamente guardado."""
    try:
        modelo = joblib.load(ruta)
        return modelo
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

# Función para predecir nuevos valores
def predecir(modelo, nuevos_datos):
    """Predice nuevos valores utilizando el modelo cargado."""
    return modelo.predict(nuevos_datos)

# Bloque principal para ejecutar el código
if __name__ == "__main__":
    # Ejemplo de uso
    datos = cargar_datos('ruta/del/archivo.csv')
    if datos is not None:
        X, y = preparar_datos(datos)
        modelo = entrenar_modelo(X, y)
        guardar_modelo(modelo, 'modelo_predictivo.pkl')

