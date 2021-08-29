# file: src/main.py 
# author: Josue Teodoro Moreira <teodoro.josue@protonmail.ch>
# date: Jun 27, 2021

import os
from flask import Flask, render_template

from db_handler import db_handler
from entity_handler import entity_handler

port = 3001
template_folder = os.path.abspath("web")
static_folder = os.path.abspath("web")
app = Flask(__name__, template_folder = "../web", static_folder = static_folder)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/consult")
def consult():
  return render_template("consult.html")

def init_server():
  app.run(host = "127.0.0.1", port = port)

def main():
  _db_handler = db_handler("db/", "sistema-de-cadastro", "bizo")
  _entity_handler = entity_handler(_db_handler)

  init_server()

  _db_handler.disconnect()

if __name__ == "__main__":
  main()
