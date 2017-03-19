from app.crud import ClientIO


class ButtonListener(object):

    @staticmethod
    def new_screen_update(class_name, lbl_path_class, lbl_path_method,
                          lbl_form_1, lbl_form_2, lbl_form_3, lbl_form_4,
                          form_input_1, form_input_2, form_input_3, form_input_4,
                          ):
        lbl_path_method.setText('New')
        if class_name == 'Client':
            # title
            lbl_path_class.setText('Client')
            # form labels
            lbl_form_1.setText('Name:')
            lbl_form_2.setText('Age:')
            lbl_form_3.setText('Address:')
            lbl_form_4.setText('CPF:')

            lbl_form_1.setVisible(True)
            lbl_form_2.setVisible(True)
            lbl_form_3.setVisible(True)
            lbl_form_4.setVisible(True)
            # form inputs
            form_input_1.setVisible(True)
            form_input_2.setVisible(True)
            form_input_3.setVisible(True)
            form_input_4.setVisible(True)
        elif class_name == 'Manager':
            lbl_path_class.setText('Manager')
            lbl_form_1.setText('Name:')
            lbl_form_2.setText('Email:')

            lbl_form_1.setVisible(True)
            lbl_form_2.setVisible(True)
            lbl_form_3.setVisible(False)
            lbl_form_4.setVisible(False)
            form_input_1.setVisible(True)
            form_input_2.setVisible(True)
            form_input_3.setVisible(False)
            form_input_4.setVisible(False)
        elif class_name == 'Equipment':
            lbl_path_class.setText('Equipment')
            lbl_form_1.setText('Model:')
            lbl_form_2.setText('Brand:')
            lbl_form_3.setText('Consumption:')

            lbl_form_1.setVisible(True)
            lbl_form_2.setVisible(True)
            lbl_form_3.setVisible(True)
            lbl_form_4.setVisible(False)
            form_input_1.setVisible(True)
            form_input_2.setVisible(True)
            form_input_3.setVisible(True)
            form_input_4.setVisible(False)
        elif class_name == 'Agency':
            lbl_path_class.setText('Agency')
            lbl_form_1.setText('City:')
            lbl_form_2.setText('Address:')
            lbl_form_3.setText('Manager:')

            lbl_form_1.setVisible(True)
            lbl_form_2.setVisible(True)
            lbl_form_3.setVisible(True)
            lbl_form_4.setVisible(False)
            form_input_1.setVisible(True)
            form_input_2.setVisible(True)
            form_input_3.setVisible(True)
            form_input_4.setVisible(False)
        elif class_name == 'Consumption':
            lbl_path_class.setText('Consumption')
            lbl_form_1.setText('Time:')
            lbl_form_2.setText('Consumption:')

            lbl_form_1.setVisible(True)
            lbl_form_2.setVisible(True)
            lbl_form_3.setVisible(False)
            lbl_form_4.setVisible(False)
            form_input_1.setVisible(True)
            form_input_2.setVisible(True)
            form_input_3.setVisible(False)
            form_input_4.setVisible(False)
        elif class_name == 'Support':
            lbl_path_class.setText('Support')
            lbl_form_1.setText('Call:')
            lbl_form_2.setText('Protocol:')

            lbl_form_1.setVisible(True)
            lbl_form_2.setVisible(True)
            lbl_form_3.setVisible(False)
            lbl_form_4.setVisible(False)
            form_input_1.setVisible(True)
            form_input_2.setVisible(True)
            form_input_3.setVisible(False)
            form_input_4.setVisible(False)

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

    @staticmethod
    def cancel():
        # goes to main screen
        pass
