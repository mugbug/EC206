# coding: utf-8
from crud import *


class ClientAttributeError(Exception):
    def __init__(self, message):
        super(ClientAttributeError, self).__init__(message)


class Client(object):
    # Singleton implementation
    class __Client:
        def __init__(self, name, address, cpf, age, password):
            self.name = name
            self.address = address
            self.cpf = cpf
            self.age = age
            self.password = password
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

    def __getattr__(self, item):
        raise ClientAttributeError("Access denied to 'Client' attribute '{0}'".format(item))


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

    def __init__(self, equipment_power, day, kwh_price, daily_usage, quantity):
        self.equipment_power = equipment_power
        self.day = day
        self.kwh_price = kwh_price
        self.quantity = quantity
        self.daily_usage = daily_usage
        self.total_consumption = float
        self.daily_consumption = 0
        self.monthly_consumption = 0
        self.total_cost = 0

    def calculate_consumption(self):
        # total consumption
        self.total_consumption = (float(self.quantity)*float(self.equipment_power)*float(self.daily_usage))/1000

        self.total_cost = self.total_consumption*float(self.kwh_price)
        # per equipment consumption
        # self.equipment.consumption = self.total_consumption/self.equipment.quantity

    # def update_data(self):
    #     # By equipment
    #     self.equipment_data = {
    #         self.equipment.name: [self.equipment.consumption,
    #                               self.equipment.daily_usage,
    #                               self.kwh_price*self.equipment.consumption,
    #                               ],
    #     }
    #     # By day
    #     day, month, year = self.day.split('/')
    #     for e in EquipmentIO.get_all():
    #         self.daily_consumption += e.consumption
    #     self.day_data = {
    #         day: [self.daily_consumption,
    #               self.equipment.daily_usage,
    #               self.kwh_price*self.daily_consumption,
    #               ],
    #     }
    #     # By month
    #     for c in ConsumptionIO.get_all():
    #         self.monthly_consumption += c.daily_consumption
    #     self.month_data = {
    #         month: [self.monthly_consumption,
    #                 self.equipment.daily_usage,
    #                 self.kwh_price*self.monthly_consumption,
    #                 ],
    #     }


class Support(object):
    def __init__(self, id_number, phone):
        self.id_number = id_number
        self.phone = phone
        self.protocol = []
        self.is_available = True

    def change_status(self):
        if self.is_available:
            self.is_available = False
        else:
            self.is_available = True

    def add_protocol(self, protocol):
        self.protocol.append(protocol)