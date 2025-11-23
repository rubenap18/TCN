-- Base de Datos: tcn
-- Tabla: ciudad


-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS ciudad;

-- 1. Crear la tabla ciudad
CREATE TABLE ciudad (
    codigo VARCHAR(3) NOT NULL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE
);

-- 2. Insertar los datos del catalogo de datos
INSERT INTO ciudad (codigo, nombre) VALUES
('TIJ', 'Tijuana'),
('MXL', 'Mexicali'),
('ROS', 'Rosarito'),
('SFL', 'San Felipe'),
('TEC', 'Tecate'),
('SNQ', 'San Quintin'),
('ESE', 'Ensenada');
