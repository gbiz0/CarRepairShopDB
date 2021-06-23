# file: src/db_handler.py
# author: Gustavo Bizo Jardim, Josue Teodoro Moreira
# date: Jun 21, 2021

import sqlite3
from os import path

class dbHandler:
    def __init__(self, file_path, password):
        self.file_path = file_path
        self.password = password
        self.cursor = None
        self.connection = None

    def load_script(self, file_path, script_name, script_var_list):
        script_file = open(file_path)

        script_buffer = ""
        is_reading = False
        for line in script_file:
            if script_name in line:
                is_reading = True
            elif ';' in line and is_reading:
                script_buffer = script_buffer + line

                is_reading = False
            elif is_reading:
                script_buffer = script_buffer + line
        script_file.close()

        if sqlite3.complete_statement(script_buffer):
            if script_var_list == None:
                self.cursor.execute(script_buffer)
            else:
                self.cursor.execute(script_buffer, script_var_list)
            self.connection.commit()

    def connect(self):
        is_file_new = True
        if path.exists(self.file_path):
            is_file_new = False

        try:
            self.connection = sqlite3.connect(self.file_path)
            self.cursor = self.connection.cursor()

            if is_file_new:
                self.load_script("db/script/db_handler.sql", "create_client_table", None)
                self.load_script("db/script/db_handler.sql", "create_car_table", None)
        except sqlite3.Error as e:
            print("Could not connect to database:", e.args[0])

    def disconnect(self):
        self.connection.close()