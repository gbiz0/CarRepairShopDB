# file: src/main.py 
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

import os
import threading
from flask import Flask, render_template, request

from db_handler import db_handler
from entity_handler import entity_handler

port = 3001
app = Flask("CarRepairShopDB", template_folder = os.path.abspath("web"), static_folder = os.path.abspath("web"))

_db_handler = db_handler("db/", "sistema-de-cadastro", "bizo")
_entity_handler = entity_handler(_db_handler)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/consult")
def consult():
  services = _entity_handler.get_all_services()
  
  return render_template("consult.html", services = services)

@app.route("/create-service", methods = ["POST"])
def create_service():
  # client
  name = request.form.get("name")
  cpf = request.form.get("cpf")
  address = request.form.get("address")
  phone_number = request.form.get("phone")
  
  new_client = _entity_handler.add_client(name, cpf, address, phone_number)
  if not new_client:
    return render_template("register.html",
                           message = "Não foi possível criar um novo serviço: Falha na criação do cliente")

  # car
  brand = request.form.get("brand")
  plate = request.form.get("plate")
  model = request.form.get("model")
  km = int(request.form.get("km"))
  year = int(request.form.get("year"))
  
  new_car = _entity_handler.add_car(brand, plate, year, model, km, new_client.get_id())
  if not new_car:
    return render_template("register.html",
                           message = "Não foi possível criar um novo serviço: Falha na criação do carro")

  # service
  problem = request.form.get("problem")
  price = request.form.get("price")

  new_service = _entity_handler.add_service(problem, price, new_client.get_id(), new_car.get_id())
  if not new_service:
    return render_template("register.html",
                           message = "Não foi possível criar um novo serviço")

  return render_template("register.html", message = "O novo serviço foi criado com sucesso")

def main():
  app.run(host = "127.0.0.1", port = port)

  _db_handler.disconnect()

if __name__ == "__main__":
  main()
