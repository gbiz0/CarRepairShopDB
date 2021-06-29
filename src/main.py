# file: src/main.py 
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

from handler import db_handler, entity_handler

def main():
  _db_handler = db_handler("db/", "test", "jhon")
  _entity_handler = entity_handler(_db_handler)
  
  josh = _entity_handler.add_client("Josue Teodoro Moreira", "88888888888", "Nowhere St.", "11999999999")
  _entity_handler.add_car("Tesla", 2021, "S", 100, josh)
  _entity_handler.update()

  _db_handler.disconnect()

if __name__ == "__main__":
  main()
