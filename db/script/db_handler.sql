/*
 * file: db/script/db_handler.sql
 * author: Gustavo Bizo Jardim, Josue Teodoro Moreira
 * date: Jun 22, 2021
 */

/* create_client_table */
create table client
(
    client_id serial,
    client_name varchar(255),
    client_cpf varchar(11),
    client_address varchar(255),
    client_phone_number varchar(14),
    constraint pk_client primary key(client_id)
);

/* create_car_table */
create table car
(
    car_id serial,
    car_brand varchar(60),
    car_year int,
    car_model varchar(50),
    car_km int,
    constraint pk_car primary key(car_id)
);