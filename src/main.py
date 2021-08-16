# file: src/main.py 
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

from db_handler import db_handler
from entity_handler import entity_handler

def main():
  _db_handler = db_handler("db/", "test", "jhon")
  _entity_handler = entity_handler(_db_handler)

  _db_handler.disconnect()

if __name__ == "__main__":
  main()
