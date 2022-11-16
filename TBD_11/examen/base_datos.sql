create database peliculas;

create table pelicula(
id int not null primary key,
nombre_pelicula varchar(30) not null,
duracion int not null,
id_genero int not null,
id_director int not null,
constraint fkdirector foreign key
);

create table direcotor(
id int not null primary key

);
