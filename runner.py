# coding: UTF-8

from models import Client

c = []


def add():
    """Creates new object of Client"""
    client = Client()
    print 'Entre com os dados:'
    client.name = raw_input('Nome:')
    client.age = input('Idade:')
    client.cpf = raw_input('CPF:')
    client.address = raw_input('Endereço: ')
    print 'Cadastrado com Sucesso!'
    c.append(client)


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


def get_all():
    """Shows all registered Client object attributes values"""
    if c is not None:
        for client in c:
            print client.__dict__
    else:
        print 'Nao tem nenhum cliente cadastrado'

if __name__ == '__main__':

    while True:
        menu_text = """Escolha o cadastro:
                    1- Cadastrar
                    2- Editar
                    3- Consultar
                    4- Excluir
                    5 - Listar
                    0 - Sair
                """
        opt = raw_input(menu_text)
        if opt == '1':
            add()
        elif opt == '2':
            update()
        elif opt == '3':
            get()
        elif opt == '4':
            delete()
        elif opt == '5':
            get_all()
        elif opt == '0':
            print 'Saindo...'
            break
        else:
            print 'Opção invalida!'

