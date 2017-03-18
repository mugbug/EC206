from app.crud import ClientIO


class ButtonListener(object):

    @staticmethod
    def add_client(name_field, address_field, cpf_field, age_field):
        name = str(name_field.text())
        address = str(address_field.text())
        cpf = str(cpf_field.text())
        age = int(age_field.text())
        if (name and address and cpf and age) != '':
            ClientIO.add(name, address, cpf, age)
            name_field.setText('')
            address_field.setText('')
            cpf_field.setText('')
            age_field.setValue(0)
        else:
            print 'ERROR: All fields must be filled!'
