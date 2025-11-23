
-- Base de Datos: tcn
-- Tabla: amenidad


-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS amenidad;

-- 1. Crear la tabla amenidad
CREATE TABLE amenidad(
    codigo VARCHAR(4) PRIMARY KEY,
    descripcion VARCHAR(25) NOT NULL
);

-- 2. Insertar los datos del catalogo de datos
INSERT INTO amenidad (codigo, descripcion) VALUES
('S44','44 Asientos'),
('AS34','34 Asientos'),	
('TOMA','Tomacorrientes'),
('PAMB','Pantallas Ambientales'),	
('PIND','Pantallas Individuales'),
('WION','WiFi a Bordo'),	
('WISA','WiFi Satelital'),
('WCUN','WC Unisex'),	
('WCIN','WC Individual')	


