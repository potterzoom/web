-- Tabla para almacenar la latencia de los servidores
CREATE TABLE IF NOT EXISTS latencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor TEXT NOT NULL,
    tiempo_respuesta REAL NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear los índices por separado
CREATE INDEX idx_latencias_servidor ON latencias(servidor);
CREATE INDEX idx_latencias_fecha_hora ON latencias(fecha_hora);

-- Tabla para almacenar la carga de los servidores
CREATE TABLE IF NOT EXISTS cargas_servidores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor TEXT NOT NULL,
    carga REAL NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear los índices por separado
CREATE INDEX idx_cargas_servidores_servidor ON cargas_servidores(servidor);
CREATE INDEX idx_cargas_servidores_fecha_hora ON cargas_servidores(fecha_hora);

-- Tabla para registrar la pérdida de paquetes
CREATE TABLE IF NOT EXISTS perdidas_paquetes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor TEXT NOT NULL,
    porcentaje_perdida REAL NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear los índices por separado
CREATE INDEX idx_perdidas_paquetes_servidor ON perdidas_paquetes(servidor);
CREATE INDEX idx_perdidas_paquetes_fecha_hora ON perdidas_paquetes(fecha_hora);

-- Tabla para almacenar la congestión de red
CREATE TABLE IF NOT EXISTS congestiones_red (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor TEXT NOT NULL,
    nivel_congestion INTEGER NOT NULL, -- 0: Normal, 1: Moderado, 2: Alto
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear los índices por separado
CREATE INDEX idx_congestiones_red_servidor ON congestiones_red(servidor);
CREATE INDEX idx_congestiones_red_fecha_hora ON congestiones_red(fecha_hora);

-- Tabla para almacenar los tiempos de respuesta de las solicitudes
CREATE TABLE IF NOT EXISTS tiempos_respuestas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor TEXT NOT NULL,
    tiempo_respuesta REAL NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear los índices por separado
CREATE INDEX idx_tiempos_respuestas_servidor ON tiempos_respuestas(servidor);
CREATE INDEX idx_tiempos_respuestas_fecha_hora ON tiempos_respuestas(fecha_hora);

-- Tabla para almacenar las alertas predictivas
CREATE TABLE IF NOT EXISTS alertas_predictivas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    servidor TEXT NOT NULL,
    tipo_alerta TEXT NOT NULL,
    nivel_riesgo INTEGER NOT NULL, -- 0: Bajo, 1: Medio, 2: Alto
    mensaje TEXT NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear los índices por separado
CREATE INDEX idx_alertas_predictivas_servidor ON alertas_predictivas(servidor);
CREATE INDEX idx_alertas_predictivas_fecha_hora ON alertas_predictivas(fecha_hora);

