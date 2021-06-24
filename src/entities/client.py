# file: src/entities/client.py
# author: Gustavo Bizo Jardim 
# date: Jun 21, 2021

import entities.car

class Client:
    def __init__(self, name, cpf, address, phone_number, db_handler):
        self.id = None
        self.name = name
        self.cpf = cpf
        self.address = address
        self.phone_number = phone_number
        self.cars = [None]
        self.db_handler = db_handler
        self.should_update = False

        if db_handler != None:
            try:
                db_handler.load_script("db/script/client.sql", "insert_new_client",
                                       {
                                           "name": self.get_name(),
                                           "cpf": self.get_cpf(),
                                           "address": self.get_address(),
                                           "phone_number": self.get_phone_number()
                                       })

                self.id = self.get_id()
            except:
                print("Could not create new client")

    def update(self):
        if self.db_handler != None and self.should_update == True:
            try:
                self.db_handler.load_script("db/script/client.sql", "update_client",
                                            {
                                                "name": self.get_name(),
                                                "cpf": self.get_cpf(),
                                                "address": self.get_address(),
                                                "phone_number": self.get_phone_number(),
                                                "id": self.get_id()
                                            })
                self.should_update = False
            except:
                print("Could not update client")

    def get_id(self):
        if self.id != None:
            return self.id
        else:
            try:
                self.id = self.db_handler.load_script("db/script/client.sql", "get_client_id",
                                                      { "cpf": self.get_cpf() })[0]
            except:
                print("Could not get client id")

    def get_name(self):
        return self.name

    def set_name(self, name):
        if self.name != name:
            self.name = name
            self.should_update = True

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        if self.cpf != cpf:
            self.cpf = cpf
            self.should_update = True

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
