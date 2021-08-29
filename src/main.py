# file: src/main.py 
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

import os
import threading
from flask import Flask, render_template, request

from db_handler import db_handler
from entity_handler import entity_handler

port = 3001
template_folder = os.path.abspath("web")
static_folder = os.path.abspath("web")
app = Flask(__name__, template_folder = "../web", static_folder = static_folder)

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
  return render_template("consult.html")

@app.route("/create-service", methods = ["POST"])
def create_service():
  name = request.form.get("name")
  cpf = request.form.get("cpf")
  address = request.form.get("address")
  phone_number = request.form.get("phone")
  
  return render_template("register.html")

def main():
  app.run(host = "127.0.0.1", port = port)

  _db_handler.disconnect()

if __name__ == "__main__":
  main()
