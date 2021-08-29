/**
 * file: src/db/service_queries.sql
 * author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
 * date: August 29, 2021
 */

/* create_service_table */
create table service
(
  service_id      integer primary key unique,
  service_problem varchar not null,
  service_price   float   not null,
  service_car     integer not null,
  service_client  integer not null,
  foreign key(service_car) references car(car_id),
  foreign key(service_client) references client(client_id)
);

/* insert_new_service */
insert into service
(
  service_problem,
  service_price,
  service_car,
  service_client
)
values
(
  :problem,
  :price,
  :car,
  :client
);

/* get_service_id */
select service_id
from service
where service_problem = :problem and
      service_price   = :price   and
      service_car     = :car     and
      service_client  = :client;

/* get_all_services */
select *
from service;

/* update_service */
update service
set service_problem = :problem,
    service_price   = :price,
    service_car     = :car,
    service_client  = :client;

/* count_services */
select count(*)
from service;

/* delete_service_with_id */
delete from service
where service_id = :id;
