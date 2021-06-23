/*
 * file: db/script/client.sql
 * author: Gustavo Bizo Jardim, Josue Teodoro Moreira
 * date: Jun 22, 2021
 */

/* insert_new_client */
insert into client
(
    client_name,
    client_address,
    client_phone_number
)
values
(
    :client_name,
    :client_address,
    :client_phone_number
);