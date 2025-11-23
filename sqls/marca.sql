
-- Base de Datos: tcn
-- Tabla: marca

-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS marca;

-- 1. Crear la tabla marca
CREATE TABLE marca (
    codigo VARCHAR(4) PRIMARY KEY,
    descripcion VARCHAR(10) NOT NULL,
    porcentajeDesc INT NOT NULL
);

-- 2. Insertar los datos del catalogo
INSERT INTO marca (codigo, descripcion, porcentajeDesc) VALUES
('ADUL', 'ADULTO', 50),
('NIÑO', 'NIÑO', 0),
('3DAD', '3ERA EDAD', 50);