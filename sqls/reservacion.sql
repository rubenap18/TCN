-- tabla: reservacion
-- BD: tcn

DROP TABLE IF EXISTS reservacion;


CREATE TABLE reservacion (
    numero INT PRIMARY KEY AUTO_INCREMENT, 
    fecha DATE NOT NULL, 
    fechaLimPago DATE NOT NULL, 
    cantPasajeros INT NOT NULL, 
    subtotal DECIMAL(6, 2) NOT NULL, 
    IVA DECIMAL(6, 2) NOT NULL, 
    total DECIMAL(7, 2) NOT NULL, 
    pasajero INT NOT NULL, 
    corrida VARCHAR(10) NOT NULL
);

-- 1. Añadir la restricción para pasajero
ALTER TABLE reservacion
ADD CONSTRAINT fk_reserva_pasajero
FOREIGN KEY (pasajero)
REFERENCES pasajero(numero); -- Asumo que la PK de PASAJERO es 'numero'

-- 2. Añadir la restricción para corrida
ALTER TABLE reservacion
ADD CONSTRAINT fk_reserva_corrida
FOREIGN KEY (corrida)
REFERENCES corrida(codigo); -- La PK de CORRIDA es 'codigo'

INSERT INTO reservacion (fecha, `fechaLimPago`,`cantPasajeros`,subtotal,`IVA`,total,pasajero,corrida) VALUES 
(DATE_FORMAT(fecha,'%d%m%Y'),DATE_FORMAT(`fechaLimPago`,'%d%m%Y'),1,,16)

SELECT c.`tarifaBase`
FROM corrida as c
WHERE c.codigo = 'ESE-MXL-01'

