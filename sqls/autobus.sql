-- TABLA: autobus

DROP TABLE IF EXISTS autobus;

CREATE TABLE autobus (
    numero VARCHAR(3) PRIMARY KEY,
    matricula VARCHAR(10) NOT NULL UNIQUE,
    claveWIFI VARCHAR(20),
    cantAsientos INT NOT NULL,
    asientosDisp INT NOT NULL,
    tipoAutobus VARCHAR(4) NOT NULL,
    estado VARCHAR(4) NOT NULL,
    marca VARCHAR(5) NOT NULL,
    modelo VARCHAR(5) NOT NULL
);

INSERT INTO autobus (numero, matricula, claveWIFI, cantAsientos, asientosDisp, tipoAutobus, estado, marca, modelo) VALUES
(100, 'TU87Y6', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'VOLVO', 'V9800'),
(104, 'UY767Y', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'VOLVO', 'V9800'),
(106, 'ERT56T', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'IRIZA', 'IRIZ6'),
(118, 'BC09IJ', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'IRIZA', 'IRIZ6'),
(130, 'DE29XU', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'IRIZA', 'IRIZ6'),
(164, 'CA980M', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'VOLVO', 'V9800'),
(170, 'MX89NL', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'VOLVO', 'V9800'),
(181, 'FG098T', 'TCNMELLEVA', 44, 44, 'PLUS', 'ACT', 'IRIZA', 'IRIZ6'),
(502, 'OSF87U', 'TCNMELLEVA', 34, 34, 'PLAT', 'ACT', 'VOLVO', 'V98DD'),
(509, 'AHL76J', 'TCNMELLEVA', 34, 34, 'PLAT', 'ACT', 'IRIZA', 'IRIZ8'),
(520, 'GHY700', 'TCNMELLEVA', 34, 34, 'PLAT', 'ACT', 'IRIZA', 'IRIZ8'),
(581, 'HUH78K', 'TCNMELLEVA', 34, 34, 'PLAT', 'ACT', 'SCANI', 'EU5DD');

#FORANEAS
-- 1. Añadir la restricción para tipoAutobus
ALTER TABLE autobus
ADD CONSTRAINT fk_tipoAutobus
FOREIGN KEY autobus(tipoAutobus)
REFERENCES tipo_autobus(codigo)
ON UPDATE CASCADE ON DELETE RESTRICT;

-- 2. Añadir la restricción para estado
ALTER TABLE autobus
ADD CONSTRAINT fk_estadoAutobus
FOREIGN KEY autobus(estado)
REFERENCES edo_autobus(codigo)
ON UPDATE CASCADE ON DELETE RESTRICT;

-- 3. Añadir la restricción para marca
ALTER TABLE autobus
ADD CONSTRAINT fk_marcaAutobus
FOREIGN KEY (marca)
REFERENCES marca(clave)
ON UPDATE CASCADE ON DELETE RESTRICT;

-- 4. Añadir la restricción para modelo
ALTER TABLE autobus
ADD CONSTRAINT fk_modeloAutobus
FOREIGN KEY (modelo)
REFERENCES modelo(clave)
ON UPDATE CASCADE ON DELETE RESTRICT;