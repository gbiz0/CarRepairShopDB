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
        should_return = False
        for line in script_file:
            if script_name in line:
                is_reading = True
            elif ';' in line and is_reading:
                script_buffer = script_buffer + line

                is_reading = False
            elif is_reading:
                if "select" in line or "SELECT" in line:
                    should_return = True

                script_buffer = script_buffer + line
        script_file.close()

        return_buffer = None
        if sqlite3.complete_statement(script_buffer):
            try:
                if script_var_list == None:
                    return_buffer = self.cursor.execute(script_buffer)
                else:
                    return_buffer = self.cursor.execute(script_buffer, script_var_list)
            except sqlite3.Error as e:
                print("Could not run script:", script_name, "->", e.args[0])
            self.connection.commit()

        if should_return:
            return return_buffer.fetchall()

    def connect(self):
        is_file_new = True
        if path.exists(self.file_path):
            is_file_new = False

        try:
            sqlite3.paramstyle = "named"
            self.connection = sqlite3.connect(self.file_path)
            self.connection.row_factory = lambda cursor, row: row[0]
            self.cursor = self.connection.cursor()

            if is_file_new:
                self.load_script("db/script/db_handler.sql", "create_client_table", None)
                self.load_script("db/script/db_handler.sql", "create_car_table", None)
        except sqlite3.Error as e:
            print("Could not connect to database:", e.args[0])

    def disconnect(self):
        self.connection.close()
