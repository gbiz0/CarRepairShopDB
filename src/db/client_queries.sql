/**
 * file: src/db/client_queries.sql
 * author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
 * date: Jun 27, 2021
 */

/* create_client_table */
create table client
(
  client_id           integer      primary key unique,
  client_name         varchar(255) not null unique,
  client_cpf          char(11)     not null unique,
  client_address      varchar(255) not null,
  client_phone_number char(11)
);

/* insert_new_client */
insert into client
(
  client_name,
  client_cpf,
  client_address,
  client_phone_number
)
values
(
  :name,
  :cpf,
  :address,
  :phone_number
);

/* get_client_id */
select client_id
from client
where
client_name         = :name    and
client_cpf          = :cpf     and
client_address      = :address and
client_phone_number = :phone_number;

/* get_all_clients */
select *
from client;

/* update_client */
update client
set client_name         = :name,
    client_address      = :address,
    client_phone_number = :phone_number
where client_id         = :id;

/* count_clients */
select count(*)
from client;

/* delete_client_with_id */
delete from client
where client_id = :id;
