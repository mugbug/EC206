# coding: UTF-8

from models import *


c = []

class Client(object):

    @staticmethod
    def add():
        """Creates new object of Client"""

        print 'Entre com os dados:'
        name = raw_input('Nome:')
        age = input('Idade:')
        cpf = raw_input('CPF:')
        address = raw_input('Endereço: ')
        client = Client(name, age, cpf, address)
        c.append(client)
        print 'Cadastrado com Sucesso!'

    @staticmethod
    def update():
        """Lets user change some Client objects attributes"""

        name = raw_input('Nome do cliente para editar:')
        flag = 0
        for client in c:
            if name == client.name:
                print 'Entre com os novos dados do cliente:'
                client.name = raw_input('Nome:')
                client.age = input('Idade:')
                client.cpf = raw_input('CPF:')
                client.address = raw_input('Endereço: ')
                print 'Editado com Sucesso!'
                flag = 1
        if flag == 0:
            print 'Cliente não encontrado!'

    @staticmethod
    def delete():
        """Removes the Client object from data base"""

        name = raw_input('Nome do cliente para remover:')
        flag = 0
        for client in c:
            if name == client.name:
                c.remove(client)
                flag = 1
        if flag == 0:
            print 'Cliente não encontrado!'

    @staticmethod
    def get():
        """Shows Client object attributes values"""

        name = raw_input('Nome do cliente para consultar:')
        flag = 0
        for client in c:
            if name == client.name:
                print client.__dict__
                flag = 1
        if flag == 0:
            print 'Cliente não encontrado!'

    @staticmethod
    def get_all():
        """Shows all registered Client object attributes values"""

        if c is not None:
            for client in c:
                print client.__dict__
        else:
            print 'Nao tem nenhum cliente cadastrado'
