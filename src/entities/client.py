# file: src/entities/client.py
# author: Gustavo Bizo Jardim 
# date: Jun 21, 2021

import sqlite3
import entities.car

class Client:
    def __init__(self, name, cpf, address, phone_number):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.phone_number = phone_number
        self.cars = [None]

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cpf(self):
        return self.cpf
        
    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_address(self):
        return self.address
        
    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number
        
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


    def add_car(self, car):
            if car is not None:
                try:
                    self.cars.append(car)
                except:
                    print("Could not add car")
            else:
                  print("Could not add car: car does not exist")

    def remove_car(self, car):
        is_car_in_array = False

        if car is not None:
            for c in self.cars:
                if c is car:
                    try:
                        self.cars.remove(c)

                        is_car_in_array = True
                    except:
                        print ("Could not remove car")

            if is_car_in_array == False:
                print("Could not remove car: car is not in car array")

        else:
                  print("Could not add car: car does not exist")
