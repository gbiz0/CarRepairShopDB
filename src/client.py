# file: src/client.py
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

class client:
  def __init__(self, id, name, cpf, address, phone_number, db_handler):
    self.id = id
    self.name = name
    self.cpf = cpf
    self.address = address
    self.phone_number = phone_number
    self.should_update = False
    self.db_handler = db_handler
    self.insert_client()

  def insert_client(self):
    if self.get_id() == 0 and self.get_db_handler() != None:
      self.db_handler.run_sql_query("insert_new_client",
                                    {
                                      "name": self.get_name(),
                                      "cpf": self.get_cpf(),
                                      "address": self.get_address(),
                                      "phone_number": self.get_phone_number()
                                    })

      # NOTE(all): This can run once or until the client values aren't changed.
      self.id = self.db_handler.run_sql_query("get_client_id",
                                              {
                                                "name": self.get_name(),
                                                "cpf": self.get_cpf(),
                                                "address": self.get_address(),
                                                "phone_number": self.get_phone_number()
                                              })[0][0]

  def update(self):
    if self.should_update:
      self.db_handler.run_sql_query("update_client",
                                    {
                                      "name": self.get_name(),
                                      "address": self.get_address(),
                                      "phone_number": self.get_phone_number(),
                                      "id": self.get_id()
                                    })

  def get_db_handler(self):
    return self.db_handler

  def set_db_handler(self, db_handler):
    should_insert_client = False
    if not self.db_handler:
      should_insert_client = True

    if self.db_handler != db_handler:
      self.db_handler = db_handler
      if should_insert_client:
        self.insert_client()

  def get_id(self):
    return self.id

  def get_name(self):
    return self.name

  def set_name(self, name):
    if self.name != name:
      self.name = name
      self.should_update = True

  def get_cpf(self):
    return self.cpf

  def get_address(self):
    return self.address

  def set_address(self, address):
    if self.address != address:
      self.address = address
      self.should_update = True

  def get_phone_number(self):
    return self.phone_number

  def set_phone_number(self, phone_number):
    if self.phone_number != phone_number:
      self.phone_number = phone_number
      self.should_update = True
