# file: src/car.py
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

class car:
  def __init__(self, id, brand, year, model, km, owner, db_handler):
    self.id = id
    self.brand = brand
    self.year = year
    self.model = model
    self.km = km
    self.owner = owner
    self.should_update = False
    self.db_handler = db_handler
    self.insert_car()

  def insert_car(self):
    if self.get_id() == 0 and self.get_db_handler() != None:
      self.db_handler.run_sql_query("insert_new_client",
                                    {
                                      "brand": self.get_brand(),
                                      "year": self.get_year(),
                                      "model": self.get_model(),
                                      "km": self.get_km(),
                                      "owner": self.get_owner()
                                    })

      # NOTE(all): This can run once or until the client values aren't changed.
      self.id = self.db_handler.run_sql_query("get_car_id",
                                              {
                                                "brand": self.get_brand(),
                                                "year": self.get_year(),
                                                "model": self.get_model(),
                                                "km": self.get_km(),
                                                "owner": self.get_owner()
                                              })[0][0]

  def update(self):
    if self.should_update:
      self.db_handler.run_sql_query("update_car",
                                    {
                                      "brand": self.get_brand(),
                                      "year": self.get_year(),
                                      "model": self.get_model(),
                                      "km": self.get_km(),
                                      "owner": self.get_owner()
                                    })

  def get_db_handler(self):
    return self.db_handler

  def set_db_handler(self, db_handler):
    should_insert_car = False
    if not self.db_handler:
      should_insert_client = True

    if self.db_handler != db_handler:
      self.db_handler = db_handler
      if should_insert_client:
        self.insert_client()

  def get_id(self):
    return self.id

  def get_brand(self):
    return self.brand

  def set_brand(self, brand):
    if self.brand != brand:
      self.brand = brand
      self.should_update = True

  def get_year(self):
    return self.year

  def set_year(self, year):
    if self.year != year:
      self.year = year
      self.should_update = True

  def get_model(self):
    return self.model

  def set_model(self, model):
    if self.model != model:
      self.model = model
      self.should_update = True

  def get_km(self):
    return self.km

  def set_km(self, km):
    if self.km != km:
      self.km = km
      self.should_update = True

  def get_owner(self):
    return self.owner

  def set_owner(self, owner):
    if self.owner != owner:
      self.owner = owner
      self.should_update = True
