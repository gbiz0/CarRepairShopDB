/*
 * file: db/script/client.sql
 * author: Gustavo Bizo Jardim, Josue Teodoro Moreira
 * date: Jun 22, 2021
 */

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

/* update_client */
update client
set client_name = :name,
    client_cpf = :cpf,
    client_address = :address,
    client_phone_number = :phone_number
where client_id = :id;

/* get_client_id */
select client_id
from client
where client_cpf = :cpf;
