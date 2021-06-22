# file: src/db_handler.py
# author: Gustavo Bizo Jardim 
# date: Jun 21, 2021

class dbHandler:
    def __init__(self, file_path, password):
        self.file_path = file_path
        self.password = password
        self.cursor = None
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.file_path)
        except:
            print("Could not connect to database")

    def disconnect(self):
        pass