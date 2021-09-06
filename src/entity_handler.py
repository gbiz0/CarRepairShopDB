# file: src/entity_handler.py
# author: Josue teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jul 17, 2021

from client import client
from car import car
from service import service

import gc

class entity_handler:
  def __init__(self, db_handler):
    self.db_handler = db_handler
    self.clients = []
    self.cars = []
    self.services = []

    if not self.db_handler.is_new():
      self.load_clients()
      self.load_cars()
      self.load_services()

  def load_clients(self):
    loaded_clients = self.db_handler.run_sql_query("get_all_clients", None)
    for client in loaded_clients:
      self.add_client_with_id(client[0], client[1], client[2], client[3], client[4])

  def load_cars(self):
    loaded_cars = self.db_handler.run_sql_query("get_all_cars", None)
    for car in loaded_cars:
      self.add_client_with_id(car[0], car[1], car[2], car[3], car[4])

  def load_services(self):
    loaded_services = self.db_handler.run_sql_query("get_all_services", None)
    for service in loaded_services:
      self.add_service_with_id(service[0], service[1], service[2], service[3], service[4])

  # client
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

  # car
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

  # service
  def get_service(self, id):
    if len(self.services) > 0:
      for service in self.services:
        if service.get_id() == id:
          return service

      return None
    else:
      return None

  def add_service(self, problem, price, car, client):
    self.services.append(service(0, problem, price, car, client, self.db_handler))

    return self.services[-1]

  def add_service_with_id(self, id, problem, price, car, client):
    self.services.append(service(id, problem, price, car, client, self.db_handler))

    return self.services[-1]

  def get_all_services(self):
    return self.services

  def remove_service(self, id):
    service_with_id = self.get_service(id)

    if service_with_id != None:
      self.db_handler.run_sql_query("delete_service_with_id", { "id": id })

      del service_with_id
      gc.collect()
