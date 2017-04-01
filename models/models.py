class Client(object):
    # Singleton implementation
    class __Client:
        def __init__(self, name, address, cpf, age):
            self.name = name
            self.address = address
            self.cpf = cpf
            self.age = age
    instance = None

    def __init__(self, name, address, cpf, age):
        if not Client.instance:
            Client.instance = Client.__Client(name, address, cpf, age)
        else:
            Client.instance.name = name
            Client.instance.address = address
            Client.instance.cpf = cpf
            Client.instance.age = age


class Manager(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Equipment(object):
    def __init__(self, model, brand, consumption):
        self.model = model
        self.brand = brand
        self.consumption = consumption


class Agency(object):
    def __init__(self, city, address, manager):
        self.city = city
        self.address = address
        self.manager = manager


class Consumption(object):
    def __init__(self, time, consumption):
        self.time = time
        self.consumption = consumption


class Support(object):
    def __init__(self, call, protocol):
        self.call = call
        self.protocol = protocol
