/*
 * file: db/script/db_handler.sql
 * author: Gustavo Bizo Jardim, Josue Teodoro Moreira
 * date: Jun 22, 2021
 */

/* create_client_table */
create table client
(
    client_id integer primary key,
    client_name varchar(255),
    client_cpf char(11),
    client_address varchar(255),
    client_phone_number char(14)
);

/* create_car_table */
create table car
(
    car_id integer primary key,
    car_brand varchar(127),
    car_year integer,
    car_model varchar(127),
    car_km integer
);
