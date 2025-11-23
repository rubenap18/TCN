
-- Base de Datos: tcn
-- Tabla: edo_corrida

-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS edo_corrida;

-- 1. Crear la tabla edo_corrida
CREATE TABLE edo_corrida(
    codigo VARCHAR(3) PRIMARY KEY,
    descripcion VARCHAR(10) NOT NULL UNIQUE
);

-- 2. Insertar los datos del catalogo de datos
INSERT INTO edo_corrida (codigo, descripcion) VALUES
('ACT', 'ACTIVO'),
('INA', 'INACTIVO')