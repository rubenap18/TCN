-- TABLA: ruta

DROP TABLE IF EXISTS ruta;

CREATE TABLE ruta (
    codigo VARCHAR(9) PRIMARY KEY,
    distancia DECIMAL(6, 2) NOT NULL,       -- Corregido a DECIMAL(6, 2) para insertar decimales
    ciudadOrigen VARCHAR(3) NOT NULL,       -- Corregido a VARCHAR(3) para coincidir con CIUDAD.codigo
    ciudadDestino VARCHAR(3) NOT NULL       -- Corregido a VARCHAR(3) para coincidir con CIUDAD.codigo
);

-- Inserción de Datos para RUTA
INSERT INTO ruta (codigo, distancia, ciudadOrigen, ciudadDestino) VALUES
('TIJ-TEC', 48.5, 'TIJ', 'TEC'),
('TIJ-ROS', 23.75, 'TIJ', 'ROS'),
('TIJ-ESE', 107.25, 'TIJ', 'ESE'),
('TIJ-MXL', 178.4, 'TIJ', 'MXL'),
('TIJ-SFL', 198.6, 'TIJ', 'SFL'),
('TIJ-SNQ', 308.9, 'TIJ', 'SNQ'),
('TEC-TIJ', 48.5, 'TEC', 'TIJ'),
('TEC-ROS', 64.8, 'TEC', 'ROS'),
('TEC-ESE', 138.2, 'TEC', 'ESE'),
('TEC-MXL', 158.75, 'TEC', 'MXL'),
('TEC-SFL', 218.45, 'TEC', 'SFL'),
('TEC-SNQ', 328.3, 'TEC', 'SNQ'),
('ROS-TIJ', 23.75, 'ROS', 'TIJ'),
('ROS-TEC', 64.8, 'ROS', 'TEC'),
('ROS-ESE', 94.6, 'ROS', 'ESE'),
('ROS-MXL', 188.9, 'ROS', 'MXL'),
('ROS-SFL', 208.75, 'ROS', 'SFL'),
('ROS-SNQ', 318.4, 'ROS', 'SNQ'),
('ESE-TIJ', 107.25, 'ESE', 'TIJ'),
('ESE-TEC', 138.2, 'ESE', 'TEC'),
('ESE-ROS', 94.6, 'ESE', 'ROS'),
('ESE-MXL', 268.5, 'ESE', 'MXL'),
('ESE-SFL', 287.8, 'ESE', 'SFL'),
('ESE-SNQ', 84.95, 'ESE', 'SNQ'),
('MXL-TIJ', 178.4, 'MXL', 'TIJ'),
('MXL-TEC', 158.75, 'MXL', 'TEC'),
('MXL-ROS', 188.9, 'MXL', 'ROS'),
('MXL-ESE', 268.5, 'MXL', 'ESE'),
('MXL-SFL', 187.35, 'MXL', 'SFL'),
('MXL-SNQ', 347.8, 'MXL', 'SNQ'),
('SFL-TIJ', 198.6, 'SFL', 'TIJ'),
('SFL-TEC', 218.45, 'SFL', 'TEC'),
('SFL-ROS', 208.75, 'SFL', 'ROS'),
('SFL-ESE', 287.8, 'SFL', 'ESE'),
('SFL-MXL', 187.35, 'SFL', 'MXL'),
('SFL-SNQ', 366.25, 'SFL', 'SNQ'),
('SNQ-TIJ', 308.9, 'SNQ', 'TIJ'),
('SNQ-TEC', 328.3, 'SNQ', 'TEC'),
('SNQ-ROS', 318.4, 'SNQ', 'ROS'),
('SNQ-ESE', 84.95, 'SNQ', 'ESE'),
('SNQ-MXL', 347.8, 'SNQ', 'MXL'),
('SNQ-SFL', 366.25, 'SNQ', 'SFL');

-- AÑADIR RESTRICCIONES FK (ALTER TABLE)
ALTER TABLE ruta
ADD CONSTRAINT fk_ruta_origen
FOREIGN KEY ruta(ciudadOrigen) 
REFERENCES ciudad(codigo)
ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE ruta
ADD CONSTRAINT fk_ruta_destino
FOREIGN KEY ruta(ciudadDestino) 
REFERENCES ciudad(codigo)
ON UPDATE CASCADE ON DELETE RESTRICT;