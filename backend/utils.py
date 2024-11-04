import numpy as np

# Datos de ejemplo para las predicciones
historial_latencias = [100, 110, 90, 120, 105]  # Datos de latencias pasadas

# Función para predecir la latencia promedio
def predecir_latencias(historial):
    return np.mean(historial)

# Definición de variables
latencias_predichas = predecir_latencias(historial_latencias)
predicciones = {"latencia": latencias_predichas}

# Funciones adicionales pueden ir aquí

# Ejemplo de uso
if __name__ == "__main__":
    print("Predicciones:", predicciones)

