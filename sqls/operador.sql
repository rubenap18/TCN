
-- Base de Datos: tcn
-- Tabla: operador


-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS operador;

-- 1. Crear la tabla operador
CREATE TABLE operador (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(15) NOT NULL,
    apellPat VARCHAR(15) NOT NULL,
    apellMat VARCHAR(15),
    fechaNac DATE NOT NULL,
    telefono VARCHAR(10) NOT NULL UNIQUE,
    fechaContrato DATE NOT NULL
);

-- 2. Insertar los datos del catalogo
INSERT INTO operador (nombre, apellPat, apellMat, fechaNac, telefono, fechaContrato) VALUES
('María', 'López', 'García', '1985-03-15', '6641234567', '2020-01-15'),
('Carlos', 'Rodríguez', 'Martínez', '1990-07-22', '6642345678', '2019-03-10'),
('Ana', 'Hernández', 'Sánchez', '1988-11-05', '6643456789', '2021-05-20'),
('Javier', 'Díaz', 'Ramírez', '1992-02-28', '6644567890', '2018-08-12'),
('Laura', 'Gómez', 'Fernández', '1987-09-14', '6645678902', '2022-02-01'),
('Miguel', 'Pérez', 'González', '1993-12-03', '6646789012', '2020-11-30'),
('Elena', 'Torres', 'Jiménez', '1991-06-18', '6647890123', '2019-07-22'),
('David', 'Ruiz', 'Moreno', '1989-04-25', '6648901234', '2021-09-05'),
('Sofía', 'Castro', 'Ortega', '1994-08-09', '6649012345', '2023-01-10'),
('Daniel', 'Mendoza', 'Silva', '1986-01-30', '6640123456', '2017-12-15'),
('Andrea', 'Reyes', 'Vargas', '1990-10-12', '6641234501', '2020-06-18'),
('Roberto', 'Núñez', 'Guerrero', '1988-05-07', '6642345601', '2019-04-14'),
('Patricia', 'Medina', 'Rojas', '1992-03-21', '6643456701', '2022-08-25'),
('Fernando', 'Cortés', 'Miranda', '1987-12-08', '6644567801', '2018-10-30'),
('Gabriela', 'Ortiz', 'Campos', '1993-09-17', '6645678901', '2021-03-12');

