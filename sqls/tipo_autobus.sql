
-- Base de Datos: tcn
-- Tabla: marca

-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS marca;

-- 1. Crear la tabla marca
CREATE TABLE marca (
    clave VARCHAR(5) PRIMARY KEY,
    nombre VARCHAR(15) NOT NULL UNIQUE
);

-- 2. Insertar los datos del catalogo
INSERT INTO marca (clave, nombre) VALUES
('VOLVO', 'VOLVO'),
('IRIZA', 'IRIZAR'),
('SCANI', 'SCANIA');