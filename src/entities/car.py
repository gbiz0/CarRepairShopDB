# file: src/entities/car.py
# author: Gustavo Bizo Jardim 
# date: Jun 21, 2021

import sqlite3

class Car:
    def __init__(self, brand, year, model, km):
        self.brand = brand
        self.year = year
        self.model = model
        self.km = km

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_km(self):
        return self.km

    def set_km(self, km):
        self.km = km
        
