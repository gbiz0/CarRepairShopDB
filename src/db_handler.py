# file: src/handler.py
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

import sqlite3
from os import path

from client import client
from car import car

class db_handler:
  def __init__(self, folder_path, file_name, username):
    if not path.exists(folder_path):
      print("Could not create database handler: given folder does not exist")
      return

    self.file_path = folder_path + file_name + ".db"
    self.username = username
    self.is_db_new = False

    self.sql_queries = {}
    self.load_sql_queries("src/db/client_queries.sql")
    self.load_sql_queries("src/db/car_queries.sql")

    sqlite3.paramstyle = "named"
    self.connection = None
    self.cursor = None
    self.connect()

  def is_new(self):
    return self.is_db_new

  def load_sql_queries(self, file_path):
    if not path.exists(file_path):
      print("Could not sql queries: file does not exist")
      return

    query_file = open(file_path)
    query_name_buffer = ""
    query_buffer = ""
    should_read = False
    for line in query_file:
      if "/*" in line and "*/" in line:
        query_name_buffer += line

        # remove /* and */
        query_name_buffer = query_name_buffer[:-4]
        query_name_buffer = query_name_buffer[3:]

        should_read = True
      elif should_read:
        query_buffer += line

        if ";" in line:
          self.sql_queries[query_name_buffer] = query_buffer
          query_buffer = ""
          query_name_buffer = ""

          should_read = False

  def run_sql_query(self, query_name, query_format):
    if query_name in self.sql_queries:
      try:
        if sqlite3.complete_statement(self.sql_queries[query_name]):
          if query_format == None:
            self.cursor.execute(self.sql_queries[query_name])
          else:
            self.cursor.execute(self.sql_queries[query_name], query_format)

          self.connection.commit()
        else:
          print("Could not run query: incomplete statement")
          return None

        if "select" in self.sql_queries[query_name] or "SELECT" in self.sql_queries[query_name]:
          return self.cursor.fetchall()
      except sqlite3.Error as err:
        print("Could not run query:", query_name, "->", err.args[0])
        print(self.sql_queries[query_name])
    else:
      print("Could not run query: query does not exist and/or could not be loaded")

  def connect(self):
    if not path.exists(self.file_path):
      self.is_db_new = True

    try:
      self.connection = sqlite3.connect(self.file_path)
      self.cursor = self.connection.cursor()

      # create new tables if new.
      if self.is_db_new:
        self.run_sql_query("create_client_table", None)
        self.run_sql_query("create_car_table", None)
    except sqlite3.Error as err:
      print("Could not connect to database:", err.args[0])

  def disconnect(self):
    self.connection.close()
