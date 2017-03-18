# coding: UTF-8
from crud import Client


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
            Client.add()
        elif opt == '2':
            Client.update()
        elif opt == '3':
            Client.get()
        elif opt == '4':
            Client.delete()
        elif opt == '5':
            Client.get_all()
        elif opt == '0':
            print 'Saindo...'
            break
        else:
            print 'Opção invalida!'
