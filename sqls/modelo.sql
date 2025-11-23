
-- Base de Datos: tcn
-- Tabla: modelo


-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS modelo;

-- 1. Crear la tabla modelo con la llaves foraneas
CREATE TABLE modelo (
    clave VARCHAR(5) PRIMARY KEY,
    nombre VARCHAR(15) NOT NULL,
    marca VARCHAR(5) NOT NULL
);

-- 2. Insertar los datos del catalogo
INSERT INTO modelo (clave,nombre,marca) VALUES
('VV980', '9800', 'VOLVO'),
('VV98D', '9800DD', 'VOLVO'),
('IRIZ8', 'i8', 'IRIZA'),
('SCA5D', '5 DD', 'SCANI');
