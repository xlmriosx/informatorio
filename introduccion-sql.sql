CREATE DATABASE ejercicio1;

CREATE TABLE clientes(
	dni INT,
    nombre CHAR(15),
    apellido CHAR(15),
    direccion CHAR(30),
    telefono INT,
    PRIMARY KEY (dni)    
);

CREATE TABLE clientes(
id INT,
precio INT,
titulo CHAR(10),
artista CHAR(15),
anio_salida INT,
PRIMARY KEY (id)
);

CREATE TABLE generos(
	nombre CHAR(10),
	ritmo CHAR(10),
	PRIMARY KEY (nombre)
);

CREATE TABLE discos(
	id INT AUTO_INCREMENT,
    genero CHAR(10), -- nombre CHAR(10),
	precio FLOAT,
	titulo CHAR(10),
	artista CHAR(15),
	anio_salida INT,
    fecha DATETIME,
	PRIMARY KEY (id),
    FOREIGN KEY (genero) REFERENCES generos(nombre)
);

INSERT INTO clientes(dni, nombre, apellido, direccion, telefono) 
VALUES(35693118,"EMILIANO","GALLARATO","CALLE FALSE 123", 12345);

ALTER TABLE discos ADD CONSTRAINT fk_genero_discos FOREIGN KEY (genero) REFERENCES generos(nombre);

-- Insertar géneros
INSERT INTO generos (nombre, ritmo)
VALUES ('Rock', 'Varios');
INSERT INTO generos (nombre, ritmo)
VALUES ('Pop', 'Varios');
INSERT INTO generos (nombre, ritmo)
VALUES ('Jazz', 'Jazz');
INSERT INTO generos (nombre, ritmo)
VALUES ('Hip-Hop', 'Hip-Hop');
INSERT INTO generos (nombre, ritmo)
VALUES ('Electronic', 'Electrónic');


-- Insertar un disco de rock
INSERT INTO discos (genero, precio, titulo, artista, anio_salida, fecha)
VALUES ('Rock', 19.99, 'Backk', 'AC/DC', 1980, '2023-10-21 10:00:00');

-- Insertar un disco de pop
INSERT INTO discos (genero, precio, titulo, artista, anio_salida, fecha)
VALUES ('Pop', 14.99, 'Thriller', 'Michael Jackson', 1982, '2023-10-21 11:15:00');

-- Insertar un disco de jazz
INSERT INTO discos (genero, precio, titulo, artista, anio_salida, fecha)
VALUES ('Jazz', 24.99, 'Kind Blue', 'Miles Davis', 1959, '2023-10-21 12:30:00');

-- Insertar un disco de hip-hop
INSERT INTO discos (genero, precio, titulo, artista, anio_salida, fecha)
VALUES ('Hip-Hop', 17.99, 'TheMarsha', 'Eminem', 2000, '2023-10-21 13:45:00');

-- Insertar un disco de electrónica
INSERT INTO discos (genero, precio, titulo, artista, anio_salida, fecha)
VALUES ('Electrónic', 12.99, 'RandomAcMe', 'Daft Punk', 2013, '2023-10-21 15:00:00');
