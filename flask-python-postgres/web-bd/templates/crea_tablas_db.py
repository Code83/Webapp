###Solo ejecutar una vez instalado el motor###

print("Solo ejecutar una vez para crear las tablas del proyecto")

sql_crea_tb_users ="CREATE TABLE public.usuarios
(
    user_id serial Primary key,
	nombre varchar[50] NOT NULL,
    apellidopat varchar[50] NOT NULL,
    apellidomat varchar[50] NOT NULL,
    rut varchar[10] NOT NULL,
    email varchar[50] NOT NULL
);

ALTER TABLE public.usuarios
    OWNER to postgres;"