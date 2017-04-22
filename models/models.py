# coding: utf-8

from crud import *


class Client(object):
    # Singleton implementation
    # add password
    # add isAdm
    class __Client:
        def __init__(self, name, address, cpf, age, password):
            self.name = name
            self.address = address
            self.cpf = cpf
            self.age = age
            self.password = password

        def __init__(self, name, address, cpf, age):
            self.name = name
            self.address = address
            self.cpf = cpf
            self.age = age
    instance = None

    def __init__(self, name, address, cpf, age, password):
        if not Client.instance:
            Client.instance = Client.__Client(name, address, cpf, age, password)
        else:
            Client.instance.name = name
            Client.instance.address = address
            Client.instance.cpf = cpf
            Client.instance.age = age
            Client.instance.password = password

    def __init__(self, name, address, cpf, age):
        if not Client.instance:
            Client.instance = Client.__Client(name, address, cpf, age)
        else:
            Client.instance.name = name
            Client.instance.address = address
            Client.instance.cpf = cpf
            Client.instance.age = age


class Manager(Client):

    class __Manager:
        def __init__(self, name, address, cpf, age, password, agency):
            self.super().__init__(name, address, cpf, age, password)
            self.agency = agency
    instance = None

    def __init__(self, name, address, cpf, age, password, agency):
        if not Manager.instance:
            Manager.instance = Manager.__Manager(name, address, cpf, age, password, agency)
        else:
            Manager.instance.name = name
            Manager.instance.address = address
            Manager.instance.cpf = cpf
            Manager.instance.age = age
            Manager.instance.password = password
            Manager.instance.agency = agency


class Equipment(object):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def average_consumption(self):
        pass

    def average_cost(self):
        pass


class Agency(object):
    def __init__(self, address, city):
        self.address = address
        self.city = city


class Consumption(object):
    def __init__(self, equipment, day, kwh_price, daily_usage, quantity):
        self.equipment = equipment
        self.day = day
        self.kwh_price = kwh_price
        self.quantity = quantity
        self.daily_usage = daily_usage
        self.total_consumption = float
        self.daily_consumption = 0
        self.monthly_consumption = 0

    def calculate_consumption(self):
        # total consumption
        self.total_consumption = (self.equipment.quantity * self.equipment.power * self.equipment.daily_usage)/1000
        # per equipment consumption
        self.equipment.consumption = self.total_consumption/self.equipment.quantity

    def update_data(self):
        # By equipment
        self.equipment_data = {
            self.equipment.name: [self.equipment.consumption,
                                  self.equipment.daily_usage,
                                  self.kwh_price*self.equipment.consumption,
                                  ],
        }
        # By day
        day, month, year = self.day.split('/')
        for e in EquipmentIO.get_all():
            self.daily_consumption += e.consumption
        self.day_data = {
            day: [self.daily_consumption,
                  self.equipment.daily_usage,
                  self.kwh_price*self.daily_consumption,
                  ],
        }
        # By month
        for c in ConsumptionIO.get_all():
            self.monthly_consumption += c.daily_consumption
        self.month_data = {
            month: [self.monthly_consumption,
                    self.equipment.daily_usage,
                    self.kwh_price*self.monthly_consumption,
                    ],
        }


class Support(object):
    def __init__(self, available, protocol):
        self.available = available
        self.protocol = protocol
