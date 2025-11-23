
-- Base de Datos: tcn
-- Tabla: edo_asiento

-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS edo_asiento;


-- 1. Crear la tabla edo_asiento
CREATE TABLE edo_asiento(
    codigo VARCHAR(4) PRIMARY KEY,
    descripcion VARCHAR(10) NOT NULL UNIQUE
);

-- 2. Insertar los datos del catalogo de datos
INSERT INTO edo_asiento (codigo, descripcion) VALUES
('DISP', 'DISPONIBLE'),
('OCUP', 'OCUPADO'),
('BLOQ', 'BLOQUEADO')

