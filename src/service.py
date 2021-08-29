# file: src/service.py
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: August 29, 2021

class service:
  def __init__(self, id, problem, price, car, client, db_handler):
    self.id = id
    self.problem = problem
    self.price = price
    self.car = car
    self.client = client
    self.should_update = False
    self.db_handler = db_handler
    self.insert_service()

  def insert_service(self):
    if self.get_id() == 0 and self.get_db_handler() != None:
      self.db_handler.run_sql_query("insert_new_service",
                                    {
                                      "problem": self.get_problem(),
                                      "price": self.get_price(),
                                      "car": self.get_car(),
                                      "client": self.get_client()
                                    })
      
    # NOTE(all): This can run once or until the client values aren't changed.
    self.id = self.db_handler.run_sql_query("get_service_id",
                                            {
                                              "problem": self.get_problem(),
                                              "price": self.get_price(),
                                              "car": self.get_car(),
                                              "client": self.get_client()
                                            })

  def update(self):
    if self.should_update:
      self.db_handler.run_sql_query("update_service",
                                    {
                                      "problem": self.get_problem(),
                                      "price": self.get_price(),
                                      "car": self.get_car(),
                                      "client": self.get_client()
                                    })

  def get_db_handler(self):
    return self.db_handler

  def set_db_handler(self, db_handler):
    should_insert_service = False
    if not self.db_handler:
      sholud_insert_service = True

    if self.db_handler != db_handler:
      self.db_handler = db_handler
      if should_insert_service:
        self.insert_service()

  def get_id(self):
    return self.id

  def get_problem(self):
    return self.problem

  def set_problem(self, problem):
    if self.problem != problem:
      self.problem = problem
      self.should_update = True

  def get_price(self):
    return self.price

  def set_price(self, price):
    if self.price != price:
      self.price = price
      self.should_update = True

  def get_car(self):
    return self.car

  def set_car(self, car):
    if self.car != car:
      self.car = car
      self.should_update = True

  def get_client(self):
    return self.client

  def set_client(self, client):
    if self.client != client:
      self.client = client
      self.should_update = True
