
-- Base de Datos: tcn
-- Tabla: tipo_pasajero

-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS tipo_pasajero;

-- 1. Crear la tabla tipo_pasajero
CREATE TABLE tipo_pasajero (
    codigo VARCHAR(4) PRIMARY KEY,
    descripcion VARCHAR(10) NOT NULL,
    porcentajeDesc INT NOT NULL
);

-- 2. Insertar los datos del catalogo
INSERT INTO tipo_pasajero (codigo, descripcion, porcentajeDesc) VALUES
('ADUL', 'ADULTO', 50),
('NIÑO', 'NIÑO', 0),
('3DAD', '3ERA EDAD', 50);