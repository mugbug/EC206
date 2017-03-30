# coding: UTF-8

from models.crud import *


class ButtonListener(object):

    @staticmethod
    def add_client(class_name, form_inputs):

        if class_name == 'Client':
            name = str(form_inputs[0].text())
            age = int(form_inputs[1].text())
            address = str(form_inputs[2].text())
            cpf = str(form_inputs[3].text())
            if (name and address and cpf and age) != '':
                ClientIO.add(name, address, cpf, age)
                # field cleaner
                for field in form_inputs:
                    field.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Manager':
            name = str(form_inputs[0].text())
            email = str(form_inputs[1].text())
            if (name and email) != '':
                ManagerIO.add(name, email)
                # field cleaner
                for field in form_inputs:
                    field.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Equipment':
            model = str(form_inputs[0].text())
            brand = str(form_inputs[1].text())
            consumption = str(form_inputs[2].text())
            if (model and brand and consumption) != '':
                EquipmentIO.add(model, brand, consumption)
                # field cleaner
                for field in form_inputs:
                    field.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Agency':
            city = str(form_inputs[0].text())
            address = str(form_inputs[1].text())
            manager = str(form_inputs[2].text())
            if (city and address and manager) != '':
                AgencyIO.add(city, address, manager)
                # field cleaner
                for field in form_inputs:
                    field.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Consumption':
            time = str(form_inputs[0].text())
            consumption = str(form_inputs[1].text())
            if (time and consumption) != '':
                ConsumptionIO.add(time, consumption)
                # field cleaner
                for field in form_inputs:
                    field.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Support':
            call = str(form_inputs[0].text())
            protocol = str(form_inputs[1].text())
            if (call and protocol) != '':
                SupportIO.add(call, protocol)
                # field cleaner
                for field in form_inputs:
                    field.setText('')
            else:
                print 'ERROR: All fields must be filled!'

    @staticmethod
    def cancel():
        # goes to main screen
        pass

    @staticmethod
    def new_screen_update(class_name, lbl_path_class, lbl_path_method,
                          lbl_forms, form_inputs
                          ):
        lbl_path_method.setText('New')
        if class_name == 'Client':
            # title
            lbl_path_class.setText('Client')
            # form labels
            lbl_forms[0].setText('Name:')
            lbl_forms[1].setText('Age:')
            lbl_forms[2].setText('Address:')
            lbl_forms[3].setText('CPF:')

            lbl_forms[2].setVisible(True)
            lbl_forms[3].setVisible(True)
            # form inputs
            form_inputs[0].setVisible(True)
            form_inputs[1].setVisible(True)
            form_inputs[2].setVisible(True)
            form_inputs[3].setVisible(True)
        elif class_name == 'Manager':
            lbl_path_class.setText('Manager')
            lbl_forms[0].setText('Name:')
            lbl_forms[1].setText('Email:')

            lbl_forms[2].setVisible(False)
            lbl_forms[3].setVisible(False)
            form_inputs[0].setVisible(True)
            form_inputs[1].setVisible(True)
            form_inputs[2].setVisible(False)
            form_inputs[3].setVisible(False)
        elif class_name == 'Equipment':
            lbl_path_class.setText('Equipment')
            lbl_forms[0].setText('Model:')
            lbl_forms[1].setText('Brand:')
            lbl_forms[2].setText('Consumption:')

            lbl_forms[2].setVisible(True)
            lbl_forms[3].setVisible(False)
            form_inputs[0].setVisible(True)
            form_inputs[1].setVisible(True)
            form_inputs[2].setVisible(True)
            form_inputs[3].setVisible(False)
        elif class_name == 'Agency':
            lbl_path_class.setText('Agency')
            lbl_forms[0].setText('City:')
            lbl_forms[1].setText('Address:')
            lbl_forms[2].setText('Manager:')

            lbl_forms[2].setVisible(True)
            lbl_forms[3].setVisible(False)
            form_inputs[0].setVisible(True)
            form_inputs[1].setVisible(True)
            form_inputs[2].setVisible(True)
            form_inputs[3].setVisible(False)
        elif class_name == 'Consumption':
            lbl_path_class.setText('Consumption')
            lbl_forms[0].setText('Time:')
            lbl_forms[1].setText('Consumption:')

            lbl_forms[2].setVisible(False)
            lbl_forms[3].setVisible(False)
            form_inputs[0].setVisible(True)
            form_inputs[1].setVisible(True)
            form_inputs[2].setVisible(False)
            form_inputs[3].setVisible(False)
        elif class_name == 'Support':
            lbl_path_class.setText('Support')
            lbl_forms[0].setText('Call:')
            lbl_forms[1].setText('Protocol:')

            lbl_forms[2].setVisible(False)
            lbl_forms[3].setVisible(False)
            form_inputs[0].setVisible(True)
            form_inputs[1].setVisible(True)
            form_inputs[2].setVisible(False)
            form_inputs[3].setVisible(False)

    @staticmethod
    def search_screen_update(class_name, lbl_path_class, lbl_path_method,
                             lbl_forms, form_inputs
                             ):
        lbl_path_method.setText('Search')
        if class_name == 'Client':
            ClientIO.get()
        elif class_name == 'Manager':
            ManagerIO.get()
        elif class_name == 'Equipment':
            EquipmentIO.get()
        elif class_name == 'Agency':
            AgencyIO.get()
        elif class_name == 'Consumption':
            ConsumptionIO.get()
        elif class_name == 'Support':
            SupportIO.get()

    @staticmethod
    def update_screen_update(class_name, lbl_path_class, lbl_path_method,
                             lbl_forms, form_inputs
                             ):
        lbl_path_method.setText('Update')
        if class_name == 'Client':
            ClientIO.update()
        elif class_name == 'Manager':
            ManagerIO.update()
        elif class_name == 'Equipment':
            EquipmentIO.update()
        elif class_name == 'Agency':
            AgencyIO.update()
        elif class_name == 'Consumption':
            ConsumptionIO.update()
        elif class_name == 'Support':
            SupportIO.update()

    @staticmethod
    def remove_screen_update(class_name, lbl_path_class, lbl_path_method,
                             lbl_forms, form_inputs
                             ):
        lbl_path_method.setText('Remove')
        if class_name == 'Client':
            ClientIO.remove()
        elif class_name == 'Manager':
            ManagerIO.remove()
        elif class_name == 'Equipment':
            EquipmentIO.remove()
        elif class_name == 'Agency':
            AgencyIO.remove()
        elif class_name == 'Consumption':
            ConsumptionIO.remove()
        elif class_name == 'Support':
            SupportIO.remove()

    @staticmethod
    def list_screen_update(class_name, lbl_path_class, lbl_path_method,
                           lbl_forms, form_inputs
                           ):
        lbl_path_method.setText('List')
        if class_name == 'Client':
            ClientIO.get_all()
        elif class_name == 'Manager':
            ManagerIO.get_all()
        elif class_name == 'Equipment':
            EquipmentIO.get_all()
        elif class_name == 'Agency':
            AgencyIO.get_all()
        elif class_name == 'Consumption':
            ConsumptionIO.get_all()
        elif class_name == 'Support':
            SupportIO.get_all()
