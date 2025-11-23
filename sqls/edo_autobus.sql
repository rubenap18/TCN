-- Base de Datos: tcn
-- Tabla: edo_autobus

-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS edo_autobus;

-- 1. Crear tabla
CREATE TABLE edo_autobus (
    codigo VARCHAR(4) PRIMARY KEY,
    descripcion VARCHAR(10) NOT NULL
);


-- 2. Insertar los datos del catalogo de datos
INSERT INTO edo_autobus (codigo, descripcion) VALUES
    ('ACTI','ACTIVO'),
    ('INAC','INACTIVO');


