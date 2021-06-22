# file: src/main.py
# author: Gustavo Bizo Jardim 
# date: Jun 21, 2021

from sys import platform
import sqlite3
import entities.client
import entities.car
from db_handler import dbHandler

if platform == "linux" or platform == "linux2":
    main_db_handler = dbHandler("./db/test.db", 12345)
elif platform == "win32":
    main_db_handler = dbHandler("C:/Dev/test.db", 12345)

def main():
    main_db_handler.connect()
    
if __name__ == "__main__":
    main()
