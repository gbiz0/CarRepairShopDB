/**
 * file: src/db/car_queries.sql
 * author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
 * date: Jun 27, 2021
 */

/* create_car_table */
create table car
(
  car_id    integer      primary key unique,
  car_brand varchar(127) not null,
  car_year  integer      not null,
  car_model varchar(127) not null,
  car_km    integer      not null,
  car_owner integer      not null,
  foreign key(car_owner) references client(client_id)
);

/* insert_new_car */
insert into car
(
  car_brand,
  car_year,
  car_model,
  car_km,
  car_owner
)
values
(
  :brand,
  :year,
  :model,
  :km,
  :owner
);

/* get_car_id */
select car_id
from car
where car_brand = :brand and
      car_year  = :year  and
      car_model = :model and
      car_km    = :km    and
      car_owner = :owner;

/* get_all_cars */
select *
from car;

/* update_car */
update car
set car_brand = :brand,
    car_year  = :year,
    car_model = :model,
    car_km    = :km,
    car_owner = :owner
where car_id  = :id;

/* count_cars */
select count(*)
from car;

/* delete_car_with_id */
delete from car
where car_id = :id;
