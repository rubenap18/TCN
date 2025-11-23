
DROP TABLE IF EXISTS corrida;


CREATE TABLE corrida (
    codigo VARCHAR(10) PRIMARY KEY, -- PK: Codigo identificador de la corrida.
    fecha DATE NOT NULL, -- NOT NULL: Fecha de la corrida.
    hora_salida TIME NOT NULL, -- NOT NULL: Hora de salida.
    hora_llegada TIME NOT NULL, -- NOT NULL: Hora de llegada.
    tarifaBase DECIMAL(6, 2) NOT NULL, -- NOT NULL: Tarifa base o estándar (asumo 6 dígitos en total, 2 decimales).
    autobus VARCHAR(3), -- FK: Numero identificador del autobús.
    ruta VARCHAR(9) NOT NULL, -- FK NOT NULL: Codigo identificador de la ruta.
    operador INT, -- FK: Numero consecutivo del operador.
    estado VARCHAR(5) NOT NULL -- FK NOT NULL: Codigo identificador del estado de la corrida.
);


INSERT INTO corrida (codigo, fecha, hora_salida, hora_llegada, tarifaBase, autobus, ruta, operador, estado) VALUES
('TIJ-MXL-01', '2025-11-25', '09:00:00', '11:30:00', 350.00, '100', 'TIJ-MXL', 1, 'ACT'),
('TIJ-MXL-02', '2025-11-25', '12:00:00', '14:30:00', 450.00, '502', 'TIJ-MXL', 2, 'ACT'),
('TIJ-MXL-03', '2025-11-25', '15:00:00', '17:30:00', 350.00, '100', 'TIJ-MXL', 1, 'ACT'),
('TIJ-MXL-04', '2025-11-25', '18:00:00', '20:30:00', 350.00, '502', 'TIJ-MXL', 2, 'ACT'),
('MXL-TIJ-01', '2025-11-25', '09:00:00', '11:30:00', 450.00, '502', 'MXL-TIJ', 2, 'ACT'),
('MXL-TIJ-02', '2025-11-25', '12:00:00', '14:30:00', 350.00, '100', 'MXL-TIJ', 1, 'ACT'),
('MXL-TIJ-03', '2025-11-25', '15:00:00', '17:30:00', 450.00, '502', 'MXL-TIJ', 2, 'ACT'),
('MXL-TIJ-04', '2025-11-25', '18:00:00', '20:30:00', 350.00, '100', 'MXL-TIJ', 1, 'ACT'),
('TIJ-ESE-01', '2025-11-25', '08:00:00', '10:00:00', 250.00, '509', 'TIJ-ESE', 3, 'ACT'),
('TIJ-ESE-02', '2025-11-25', '12:00:00', '14:00:00', 250.00, '104', 'TIJ-ESE', 4, 'ACT'),
('TIJ-ESE-03', '2025-11-25', '16:00:00', '18:00:00', 350.00, '509', 'TIJ-ESE', 3, 'ACT'),
('TIJ-ESE-04', '2025-11-25', '20:00:00', '22:00:00', 250.00, '104', 'TIJ-ESE', 4, 'ACT'),
('ESE-TIJ-01', '2025-11-25', '08:00:00', '10:00:00', 250.00, '104', 'ESE-TIJ', 4, 'ACT'),
('ESE-TIJ-02', '2025-11-25', '12:00:00', '14:00:00', 350.00, '509', 'ESE-TIJ', 3, 'ACT'),
('ESE-TIJ-03', '2025-11-25', '16:00:00', '18:00:00', 250.00, '104', 'ESE-TIJ', 4, 'ACT'),
('ESE-TIJ-04', '2025-11-25', '20:00:00', '22:00:00', 350.00, '509', 'ESE-TIJ', 3, 'ACT'),
('TIJ-SQN-01', '2025-11-25', '08:00:00', '12:00:00', 550.00, '106', 'TIJ-SNQ', 5, 'ACT'),
('SNQ-TIJ-01', '2025-11-25', '14:00:00', '18:00:00', 550.00, '106', 'SNQ-TIJ', 5, 'ACT'),
('TIJ-SFL-01', '2025-11-25', '09:00:00', '13:00:00', 550.00, '164', 'TIJ-SFL', 6, 'ACT'),
('TIJ-SFL-02', '2025-11-25', '13:00:00', '17:00:00', 650.00, '581', 'TIJ-SFL', 7, 'ACT'),
('SFL-TIJ-01', '2025-11-25', '14:00:00', '18:00:00', 550.00, '164', 'SFL-TIJ', 6, 'ACT'),
('SFL-TIJ-02', '2025-11-25', '18:00:00', '22:00:00', 650.00, '581', 'SFL-TIJ', 7, 'ACT'),
('MXL-ESE-01', '2025-11-25', '08:00:00', '11:30:00', 550.00, '170', 'MXL-ESE', 8, 'ACT'),
('MXL-ESE-02', '2025-11-25', '13:00:00', '16:30:00', 650.00, '520', 'MXL-ESE', 9, 'ACT'),
('ESE-MXL-01', '2025-11-25', '08:00:00', '11:30:00', 650.00, '520', 'ESE-MXL', 9, 'ACT'),
('ESE-MXL-02', '2025-11-25', '13:00:00', '16:30:00', 550.00, '170', 'ESE-MXL', 8, 'ACT'),
('MXL-SFL-01', '2025-11-25', '07:00:00', '09:00:00', 200.00, '118', 'MXL-SFL', 10, 'ACT'),
('MXL-SFL-02', '2025-11-25', '12:00:00', '14:00:00', 200.00, '118', 'MXL-SFL', 10, 'ACT'),
('SFL-MXL-01', '2025-11-25', '09:30:00', '11:30:00', 200.00, '118', 'SFL-MXL', 10, 'ACT'),
('SFL-MXL-02', '2025-11-25', '14:30:00', '16:30:00', 200.00, '118', 'SFL-MXL', 10, 'ACT'),
('ESE-SQN-01', '2025-11-25', '10:00:00', '13:00:00', 250.00, '130', 'ESE-SNQ', 11, 'ACT'),
('SQN-ESE-01', '2025-11-25', '14:00:00', '17:00:00', 250.00, '130', 'SNQ-ESE', 11, 'ACT'),
('TIJ-TEC-01', '2025-11-25', '07:00:00', '08:00:00', 100.00, '181', 'TIJ-TEC', 12, 'ACT'),
('TEC-MXL-01', '2025-11-25', '08:30:00', '10:30:00', 250.00, '181', 'TEC-MXL', 12, 'ACT'),
('MXL-TEC-01', '2025-11-25', '11:00:00', '13:00:00', 250.00, '181', 'MXL-TEC', 12, 'ACT'),
('TEC-TIJ-01', '2025-11-25', '13:30:00', '14:30:00', 100.00, '181', 'TEC-TIJ', 12, 'ACT');


-- 1. Añadir la restriccion para autobus (Se relaciona con la PK 'numero' de la tabla AUTOBÚS)
ALTER TABLE corrida
ADD CONSTRAINT fk_corrida_autobus
FOREIGN KEY (autobus)
REFERENCES autobus(numero)
ON UPDATE CASCADE ON DELETE RESTRICT;

-- 2. Añadir la restriccion para ruta
ALTER TABLE corrida
ADD CONSTRAINT fk_corrida_ruta
FOREIGN KEY (ruta)
REFERENCES ruta(codigo)
ON UPDATE CASCADE ON DELETE RESTRICT;

-- 3. Añadir la restriccion para operador
ALTER TABLE corrida
ADD CONSTRAINT fk_corrida_operador
FOREIGN KEY (operador)
REFERENCES operador(numero)
ON UPDATE CASCADE ON DELETE RESTRICT;

-- 4. Añadir la restriccion para estado
ALTER TABLE corrida
ADD CONSTRAINT fk_corrida_estado
FOREIGN KEY (estado)
REFERENCES edo_corrida(codigo)
ON UPDATE CASCADE ON DELETE RESTRICT;