# file: src/entity_handler.py
# author: Josue teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jul 17, 2021

from client import client
from car import car

import gc

class entity_handler:
  def __init__(self, db_handler):
    self.db_handler = db_handler
    self.clients = []
    self.cars = []

    if not self.db_handler.is_new():
      self.load_clients()
      self.load_cars()

  def load_clients(self):
    loaded_clients = self.db_handler.run_sql_query("get_all_clients", None)
    for client in loaded_clients:
      self.add_client_with_id(client[0], client[1], client[2], client[3], client[4])

  def load_cars(self):
    loaded_cars = self.db_handler.run_sql_query("get_all_cars", None)
    for car in loaded_cars:
      self.add_client_with_id(car[0], car[1], car[2], car[3], car[4])

  def get_client(self, id):
    if len(self.clients) > 0:
      for client in self.clients:
        if client.get_id() == id:
          return client

      return None
    else:
      return None

  def add_client(self, name, cpf, address, phone_number):
    self.clients.append(client(0, name, cpf, address, phone_number, self.db_handler))

    return self.clients[-1]

  def add_client_with_id(self, id, name, cpf, address, phone_number):
    self.clients.append(client(id, name, cpf, address, phone_number, self.db_handler))

    return self.clients[-1]

  def remove_client(self, id):
    client_with_id = self.get_client(id)

    if client_with_id != None:
      self.db_handler.run_sql_query("delete_client_with_id", { "id": id })

      del client_with_id
      gc.collect()

  def get_car(self, id):
    if len(self.cars) > 0:
      for car in self.cars:
        if car.get_id() == id:
          return car

      return None
    else:
      return None

  def add_car(self, brand, plate, year, model, km, owner):
    self.cars.append(car(0, brand, plate, year, model, km, owner, self.db_handler))

    return self.cars[-1]

  def add_car_with_id(self, brand, plate, year, model, km, owner):
    self.cars.append(car(0, brand, plate, year, model, km, owner, self.db_handler))

    return self.cars[-1]

  def remove_car(self, id):
    car_with_id = self.get_car(id)

    if car_with_id != None:
      self.db_handler.run_sql_query("delete_car_with_id", { "id": id })

      del client_with_id
      gc.collect()
