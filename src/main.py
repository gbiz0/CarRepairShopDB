# file: src/main.py
# author: Gustavo Bizo Jardim 
# date: Jun 21, 2021

from db_handler import dbHandler
from entities.car import Car
from entities.client import Client

main_db_handler = None
test_client = None

def main():
    main_db_handler = dbHandler("db/test.db", 12345)
    main_db_handler.connect()

    test_client = Client("Josua Teodoro Moreira", "23423423434",
                         "Nobody St. 2342", "(24) 999999999", main_db_handler)
    test_client.set_name("Joshua Theodore")
    test_client.update()

    main_db_handler.disconnect()

if __name__ == "__main__":
    main()
