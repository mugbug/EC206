from app.crud import ClientIO


class ButtonListener(object):

    @staticmethod
    def add_client(name, address, cpf, age):
        ClientIO.add(str(name.text()), str(address.text()), str(cpf.text()), int(age.text()))
