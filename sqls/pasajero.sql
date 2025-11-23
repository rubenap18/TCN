
-- Base de Datos: tcn
-- Tabla: pasajero


-- 0. Opcional: Elimina la tabla si ya existe
DROP TABLE IF EXISTS pasajero;

-- 1. Crear la tabla pasajero de la info del catalogo
CREATE TABLE pasajero (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(15) NOT NULL,
    apellPat VARCHAR(15) NOT NULL,
    apellMat VARCHAR(15),
    fechaNac DATE NOT NULL,
    edad INT NOT NULL,
    correoElect VARCHAR(40) NULL,
    telefono VARCHAR(10) NOT NULL
);


-- 2. Insertar los datos del catalogo
INSERT INTO pasajero (nombre, apellPat, apellMat, fechaNac, edad, correoElect, telefono) VALUES
('Ana', 'García', 'López', '1990-05-15', 35, 'ana.garcia15@gmail.com', '6641234567'),
('Carlos', 'Martínez', 'Rodríguez', '1985-03-22', 38, 'carlos.mtz22@gmail.com', '6642345678'),
('María', 'Hernández', 'Sánchez', '1992-11-05', 31, 'maria.hdz05@gmail.com', '6643456789'),
('Javier', 'Díaz', 'González', '1988-02-28', 35, 'javier.diaz88@gmail.com', '6644567890'),
('Laura', 'Pérez', 'Fernández', '1995-09-14', 28, 'laura.perez95@gmail.com', '6645678901'),
('Miguel', 'Torres', 'Ramírez', '2018-12-03', 5, NULL, '6646789012'),
('Elena', 'Gómez', 'Jiménez', '1991-06-18', 32, 'elena.gomez18@gmail.com', '6647890123'),
('David', 'Ruiz', 'Moreno', '1987-04-25', 36, 'david.ruiz25@gmail.com', '6648901234'),
('Sofía', 'Castro', 'Ortega', '2019-08-09', 4, NULL, '6649012345'),
('Daniel', 'Mendoza', 'Silva', '1986-01-30', 37, 'daniel.mendoza30@gmail.com', '6640123456'),
('Andrea', 'Reyes', 'Vargas', '1990-10-12', 33, 'andrea.reyes12@gmail.com', '6641234501'),
('Roberto', 'Núñez', 'Guerrero', '2017-05-07', 6, NULL, '6642345601'),
('Patricia', 'Medina', 'Rojas', '1992-03-21', 31, 'patricia.medina21@gmail.com', '6643456701'),
('Fernando', 'Cortés', 'Miranda', '1987-12-08', 36, 'fernando.cortes08@gmail.com', '6644567801'),
('Gabriela', 'Ortiz', 'Campos', '1993-09-17', 30, 'gabriela.ortiz17@gmail.com', '6645678901'),
('Ricardo', 'Chávez', 'Luna', '1989-07-04', 34, 'ricardo.chavez04@gmail.com', '6646789012'),
('Isabel', 'Vega', 'Ríos', '1991-02-19', 32, 'isabel.vega19@gmail.com', '6647890123'),
('Óscar', 'Mora', 'Delgado', '1996-04-11', 27, 'oscar.mora11@gmail.com', '6648901234'),
('Claudia', 'Ramos', 'Meza', '1994-10-23', 29, 'claudia.ramos23@gmail.com', '6649012345'),
('Francisco', 'Solís', 'León', '1985-03-30', 38, 'francisco.solis30@gmail.com', '6640123456'),
('Lucía', 'Espinoza', 'Cruz', '1992-08-07', 31, 'lucia.espinoza07@gmail.com', '6641234501'),
('José', 'Navarro', 'Serrano', '1988-01-14', 35, 'jose.navarro14@gmail.com', '6642345601'),
('Karla', 'Miranda', 'Paredes', '1993-06-28', 30, 'karla.miranda28@gmail.com', '6643456701'),
('Antonio', 'Ríos', 'Mendoza', '1987-11-09', 36, 'antonio.rios09@gmail.com', '6644567801'),
('Mónica', 'Delgado', 'Orozco', '1990-09-12', 33, 'monica.delgado12@gmail.com', '6645678901'),
('Pedro', 'Salazar', 'Tapia', '2019-12-25', 4, NULL, '6646789012'),
('Teresa', 'Lara', 'Fuentes', '1991-04-18', 32, 'teresa.lara18@gmail.com', '6647890123'),
('Raúl', 'Meza', 'Cervantes', '1989-07-03', 34, 'raul.meza03@gmail.com', '6648901234'),
('Silvia', 'Orozco', 'Galván', '1994-02-16', 29, 'silvia.orozco16@gmail.com', '6649012345'),
('Alberto', 'Cervantes', 'Vázquez', '1986-05-21', 37, 'alberto.cervantes21@gmail.com', '6640123456'),
('Rosa', 'Fuentes', 'Maldonado', '1992-10-08', 31, 'rosa.fuentes08@gmail.com', '6641234501'),
('Manuel', 'Galván', 'Zamora', '2016-03-13', 7, NULL, '6642345601'),
('Eva', 'Zamora', 'Rosas', '1993-08-26', 30, 'eva.zamora26@gmail.com', '6643456701'),
('Luis', 'Rosas', 'Bravo', '1987-01-17', 36, 'luis.rosas17@gmail.com', '6644567801');