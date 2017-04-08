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
    def __init__(self, name, power, consumption):
        self.name = name
        self.power = power
        self.consumption = consumption


class Agency(object):
    def __init__(self, address, city, manager):
        self.address = address
        self.city = city
        self.manager = manager


class Consumption(object):
    def __init__(self, equipment, time, cost):
        self.equipment = equipment
        self.time = time
        self.cost = cost


class Support(object):
    def __init__(self, available, protocol):
        self.available = available
        self.protocol = protocol
