# coding: UTF-8

from models import *


c = []
m = []
e = []
cm = []
a = []
s = []


class ClientIO(object):

    @staticmethod
    def add(name, address, cpf, age):
        """Creates new object of Client"""

        client = Client(name, address, cpf, age)
        c.append(client)

    @staticmethod
    def update():
        """Lets user change some Client objects attributes"""

        name = raw_input('Client name:')
        flag = 0
        for client in c:
            if name == client.name:
                print 'Update its attributes:'
                client.set = raw_input('Name:')
                client.age = input('Age:')
                client.cpf = raw_input('CPF:')
                client.address = raw_input('Address: ')
                print 'Client updated!'
                flag = 1
        if flag == 0:
            print 'Client not found!'

    @staticmethod
    def delete():
        """Removes the Client object from data base"""

        name = raw_input('Client name:')
        flag = 0
        for client in c:
            if name == client.name:
                c.remove(client)
                flag = 1
                print 'Client removed from database!'
        if flag == 0:
            print 'Client not found!'

    @staticmethod
    def get():
        """Shows Client object attributes values"""

        name = raw_input('Client name:')
        flag = 0
        for client in c:
            if name == client.name:
                print client.__dict__
                flag = 1
        if flag == 0:
            print 'Client not found!'

    @staticmethod
    def get_all():
        """Shows all registered Client object attributes values"""

        if c is not None:
            for client in c:
                print client.__dict__
        else:
            print "There ain't no Clients registered yet"


class ManagerIO(object):

    @staticmethod
    def add(name, email):
        """Creates new object of Manager"""

        manager = Manager(name, email)
        m.append(manager)

    @staticmethod
    def update():
        """Lets user change some Manager objects attributes"""

        name = raw_input('Manager name:')
        flag = 0
        for manager in m:
            if name == manager.name:
                print 'Update manager:'
                manager.name = raw_input('Name:')
                manager.email = raw_input('Email:')
                print 'Manager updated!'
                flag = 1
        if flag == 0:
            print 'Manager not found!'

    @staticmethod
    def delete():
        """Removes the Manager object from data base"""

        name = raw_input('Manager name:')
        flag = 0
        for manager in m:
            if name == manager.name:
                m.remove(manager)
                flag = 1
                print 'Manager removed from database!'
        if flag == 0:
            print 'Manager not found!'

    @staticmethod
    def get():
        """Shows Manager object attributes values"""

        name = raw_input('Manager name:')
        flag = 0
        for manager in m:
            if name == manager.name:
                print manager.__dict__
                flag = 1
        if flag == 0:
            print 'Manager not found!'

    @staticmethod
    def get_all():
        """Shows all registered Managers object attributes values"""

        if m is not None:
            for manager in m:
                print manager.__dict__
        else:
            print "There ain't no Managers registered yet"


class EquipmentIO(object):

    @staticmethod
    def add(model, brand, consumption):
        """Creates new object of Equipment"""

        equipment = Equipment(model, brand, consumption)
        e.append(equipment)

    @staticmethod
    def update():
        """Lets user change some Equipment objects attributes"""

        model = raw_input('Equipment model:')
        flag = 0
        for equipment in e:
            if model == equipment.name:
                print 'Update equipment:'
                equipment.model = raw_input('Model:')
                equipment.brand = raw_input('Brand:')
                equipment.consumption = raw_input('Consumption:')
                print 'Equipment updated!'
                flag = 1
        if flag == 0:
            print 'Equipment not found!'

    @staticmethod
    def delete():
        """Removes the Equipment object from data base"""

        model = raw_input('Equipment model:')
        flag = 0
        for equipment in e:
            if model == equipment.name:
                e.remove(equipment)
                flag = 1
                print 'Equipment removed from database!'
        if flag == 0:
            print 'Equipment not found!'

    @staticmethod
    def get():
        """Shows Equipment object attributes values"""

        model = raw_input('Equipment model:')
        flag = 0
        for equipment in e:
            if model == equipment.name:
                print equipment.__dict__
                flag = 1
        if flag == 0:
            print 'Equipment not found!'

    @staticmethod
    def get_all():
        """Shows all registered Equipment object attributes values"""

        if e is not None:
            for equipment in e:
                print equipment.__dict__
        else:
            print "There ain't no Equipment registered yet"


class AgencyIO(object):

    @staticmethod
    def add(city, address, manager):
        """Creates new object of Agency"""

        agency = Agency(city, address, manager)
        a.append(agency)

    @staticmethod
    def update():
        """Lets user change some Agency objects attributes"""

        city = raw_input('Agency city:')
        flag = 0
        for agency in a:
            if city == agency.city:
                print 'Update agency:'
                agency.city = raw_input('City:')
                agency.address = raw_input('Address:')
                agency.manager = raw_input('Manager:')
                print 'Agency updated!'
                flag = 1
        if flag == 0:
            print 'Agency not found!'

    @staticmethod
    def delete():
        """Removes the Agency object from data base"""

        city = raw_input('Agency city:')
        flag = 0
        for agency in a:
            if city == agency.city:
                a.remove(agency)
                flag = 1
                print 'Agency removed from database!'
        if flag == 0:
            print 'Agency not found!'

    @staticmethod
    def get():
        """Shows Agency object attributes values"""

        city = raw_input('Agency city:')
        flag = 0
        for agency in a:
            if city == agency.city:
                print agency.__dict__
                flag = 1
        if flag == 0:
            print 'Agency not found!'

    @staticmethod
    def get_all():
        """Shows all registered Agency object attributes values"""

        if a is not None:
            for agency in a:
                print agency.__dict__
        else:
            print "There ain't no Agency registered yet"


class ConsumptionIO(object):

    @staticmethod
    def add(time, consumption):
        """Creates new object of Consumption"""

        consumption = Consumption(time, consumption)
        cm.append(consumption)

    @staticmethod
    def update():
        """Lets user change some Consumption objects attributes"""

        time = raw_input('Consumption time:')
        flag = 0
        for consumption in cm:
            if time == consumption.time:
                print 'Update consumption:'
                consumption.time = raw_input('Time:')
                consumption.consumption = raw_input('Consumption:')
                print 'Consumption updated!'
                flag = 1
        if flag == 0:
            print 'Consumption not found!'

    @staticmethod
    def delete():
        """Removes the Consumption object from data base"""

        time = raw_input('Consumption time:')
        flag = 0
        for consumption in cm:
            if time == consumption.time:
                cm.remove(consumption)
                flag = 1
                print 'Consumption removed from database!'
        if flag == 0:
            print 'Consumption not found!'

    @staticmethod
    def get():
        """Shows Consumption object attributes values"""

        time = raw_input('Consumption time:')
        flag = 0
        for consumption in cm:
            if time == consumption.time:
                print consumption.__dict__
                flag = 1
        if flag == 0:
            print 'Consumption not found!'

    @staticmethod
    def get_all():
        """Shows all registered Consumption object attributes values"""

        if cm is not None:
            for consumption in cm:
                print consumption.__dict__
        else:
            print "There ain't no Consumption registered yet"


class SupportIO(object):

    @staticmethod
    def add(call, protocol):
        """Creates new object of Support"""

        support = Support(call, protocol)
        s.append(support)

    @staticmethod
    def update():
        """Lets user change some Support objects attributes"""

        protocol = raw_input('Support protocol:')
        flag = 0
        for support in s:
            if protocol == support.protocol:
                print 'Update support:'
                support.call = raw_input('Call:')
                support.protocol = raw_input('Protocol:')
                print 'Support updated!'
                flag = 1
        if flag == 0:
            print 'Support not found!'

    @staticmethod
    def delete():
        """Removes the Support object from data base"""

        protocol = raw_input('Support protocol:')
        flag = 0
        for support in s:
            if protocol == support.time:
                s.remove(protocol)
                flag = 1
                print 'Consumption removed from database!'
        if flag == 0:
            print 'Consumption not found!'

    @staticmethod
    def get():
        """Shows Consumption object attributes values"""

        protocol = raw_input('Consumption protocol:')
        flag = 0
        for support in s:
            if protocol == support.protocol:
                print support.__dict__
                flag = 1
        if flag == 0:
            print 'Support protocol not found!'

    @staticmethod
    def get_all():
        """Shows all registered Support object attributes values"""

        if s is not None:
            for support in s:
                print support.__dict__
        else:
            print "There ain't no Support registered yet"
