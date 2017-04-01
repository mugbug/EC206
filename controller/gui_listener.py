# coding: UTF-8

from models.crud import *


class ButtonFeatures(object):

    @staticmethod
    def add_client(app):
        class_name = str(app.lbl_path_class.text())
        if class_name == 'Client':
            name = str(app.form_input_1.text())
            age = int(app.form_input_2.text())
            address = str(app.form_input_3.text())
            cpf = str(app.form_input_4.text())
            if (name and address and cpf and age) != '':
                ClientIO.add(name, address, cpf, age)
                # field cleaner
                app.form_input_1.setText('')
                app.form_input_2.setText('')
                app.form_input_3.setText('')
                app.form_input_4.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Manager':
            name = str(app.form_input_1.text())
            email = str(app.form_input_2.text())
            if (name and email) != '':
                ManagerIO.add(name, email)
                # field cleaner
                app.form_input_1.setText('')
                app.form_input_2.setText('')
                app.form_input_3.setText('')
                app.form_input_4.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Equipment':
            model = str(app.form_input_1.text())
            brand = str(app.form_input_2.text())
            consumption = str(app.form_input_3.text())
            if (model and brand and consumption) != '':
                EquipmentIO.add(model, brand, consumption)
                # field cleaner
                app.form_input_1.setText('')
                app.form_input_2.setText('')
                app.form_input_3.setText('')
                app.form_input_4.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Agency':
            city = str(app.form_input_1.text())
            address = str(app.form_input_2.text())
            manager = str(app.form_input_3.text())
            if (city and address and manager) != '':
                AgencyIO.add(city, address, manager)
                # field cleaner
                app.form_input_1.setText('')
                app.form_input_2.setText('')
                app.form_input_3.setText('')
                app.form_input_4.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Consumption':
            time = str(app.form_input_1.text())
            consumption = str(app.form_input_2.text())
            if (time and consumption) != '':
                ConsumptionIO.add(time, consumption)
                # field cleaner
                app.form_input_1.setText('')
                app.form_input_2.setText('')
                app.form_input_3.setText('')
                app.form_input_4.setText('')
            else:
                print 'ERROR: All fields must be filled!'

        if class_name == 'Support':
            call = str(app.form_input_1.text())
            protocol = str(app.form_input_2.text())
            if (call and protocol) != '':
                SupportIO.add(call, protocol)
                # field cleaner
                app.form_input_1.setText('')
                app.form_input_2.setText('')
                app.form_input_3.setText('')
                app.form_input_4.setText('')
            else:
                print 'ERROR: All fields must be filled!'

    @staticmethod
    def cancel(app):
        app.widget_add.setVisible(False)
        app.widget_login.setVisible(True)

    @staticmethod
    def new_screen_update(class_name, app):
        SwitchWidget.login2new(app)
        app.lbl_path_method.setText('New')
        if class_name == 'Client':
            # title
            app.lbl_path_class.setText('Client')
            # form labels
            app.lbl_form_1.setText('Name:')
            app.lbl_form_2.setText('Age:')
            app.lbl_form_3.setText('Address:')
            app.lbl_form_4.setText('CPF:')
            app.lbl_form_1.setVisible(True)
            app.lbl_form_2.setVisible(True)
            app.lbl_form_3.setVisible(True)
            app.lbl_form_4.setVisible(True)
            app.form_input_1.setVisible(True)
            app.form_input_2.setVisible(True)
            app.form_input_3.setVisible(True)
            app.form_input_4.setVisible(True)

        elif class_name == 'Manager':
            app.lbl_path_class.setText('Manager')
            app.lbl_form_1.setText('Name:')
            app.lbl_form_2.setText('Email:')
            app.lbl_form_1.setVisible(True)
            app.lbl_form_2.setVisible(True)
            app.lbl_form_3.setVisible(False)
            app.lbl_form_4.setVisible(False)
            app.form_input_1.setVisible(True)
            app.form_input_2.setVisible(True)
            app.form_input_3.setVisible(False)
            app.form_input_4.setVisible(False)

        elif class_name == 'Equipment':
            app.lbl_path_class.setText('Equipment')
            app.lbl_form_1.setText('Model:')
            app.lbl_form_2.setText('Brand:')
            app.lbl_form_3.setText('Consumption:')
            app.lbl_form_1.setVisible(True)
            app.lbl_form_2.setVisible(True)
            app.lbl_form_3.setVisible(True)
            app.lbl_form_4.setVisible(False)
            app.form_input_1.setVisible(True)
            app.form_input_2.setVisible(True)
            app.form_input_3.setVisible(True)
            app.form_input_4.setVisible(False)

        elif class_name == 'Agency':
            app.lbl_path_class.setText('Agency')
            app.lbl_form_1.setText('City:')
            app.lbl_form_2.setText('Address:')
            app.lbl_form_3.setText('Manager:')
            app.lbl_form_1.setVisible(True)
            app.lbl_form_2.setVisible(True)
            app.lbl_form_3.setVisible(True)
            app.lbl_form_4.setVisible(False)
            app.form_input_1.setVisible(True)
            app.form_input_2.setVisible(True)
            app.form_input_3.setVisible(True)
            app.form_input_4.setVisible(False)

        elif class_name == 'Consumption':
            app.lbl_path_class.setText('Consumption')
            app.lbl_form_1.setText('Time:')
            app.lbl_form_2.setText('Consumption:')
            app.lbl_form_1.setVisible(True)
            app.lbl_form_2.setVisible(True)
            app.lbl_form_3.setVisible(False)
            app.lbl_form_4.setVisible(False)
            app.form_input_1.setVisible(True)
            app.form_input_2.setVisible(True)
            app.form_input_3.setVisible(False)
            app.form_input_4.setVisible(False)

        elif class_name == 'Support':
            app.lbl_path_class.setText('Support')
            app.lbl_form_1.setText('Call:')
            app.lbl_form_2.setText('Protocol:')
            app.lbl_form_1.setVisible(True)
            app.lbl_form_2.setVisible(True)
            app.lbl_form_3.setVisible(False)
            app.lbl_form_4.setVisible(False)
            app.form_input_1.setVisible(True)
            app.form_input_2.setVisible(True)
            app.form_input_3.setVisible(False)
            app.form_input_4.setVisible(False)

    @staticmethod
    def search_screen_update(class_name, app):
        app.lbl_path_method.setText('Search')
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
    def update_screen_update(class_name, app):
        app.lbl_path_method.setText('Update')
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
    def remove_screen_update(class_name, app):
        app.lbl_path_method.setText('Remove')
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
    def list_screen_update(class_name, app):
        app.lbl_path_method.setText('List')
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


class ButtonListener(object):
    @staticmethod
    def action_listener(app):
        # ############################# #
        #               New             #
        # ############################# #
        app.menu_file_new_client.triggered.connect(lambda: ButtonFeatures.new_screen_update('Client', app))
        app.menu_file_new_manager.triggered.connect(lambda: ButtonFeatures.new_screen_update('Manager', app))
        app.menu_file_new_equipment.triggered.connect(lambda: ButtonFeatures.new_screen_update('Equipment', app))
        app.menu_file_new_agency.triggered.connect(lambda: ButtonFeatures.new_screen_update('Agency', app))
        app.menu_file_new_consumption.triggered.connect(lambda: ButtonFeatures.new_screen_update('Consumption', app))
        app.menu_file_new_support.triggered.connect(lambda: ButtonFeatures.new_screen_update('Support', app))
        # ############################# #
        #             Search            #
        # ############################# #

        app.menu_edit_search_client.triggered.connect(lambda: ButtonFeatures.search_screen_update('Client', app))
        app.menu_edit_search_manager.triggered.connect(lambda: ButtonFeatures.search_screen_update('Manager', app))
        app.menu_edit_search_equipment.triggered.connect(lambda: ButtonFeatures.search_screen_update('Equipment', app))
        app.menu_edit_search_agency.triggered.connect(lambda: ButtonFeatures.search_screen_update('Agency', app))
        app.menu_edit_search_consumption.triggered.connect(lambda: ButtonFeatures.search_screen_update('Consumption', app))
        app.menu_edit_search_support.triggered.connect(lambda: ButtonFeatures.search_screen_update('Support', app))
        # ############################# #
        #             Update            #
        # ############################# #

        app.menu_edit_update_client.triggered.connect(lambda: ButtonFeatures.update_screen_update('Client', app))
        app.menu_edit_update_manager.triggered.connect(lambda: ButtonFeatures.update_screen_update('Manager', app))
        app.menu_edit_update_equipment.triggered.connect(lambda: ButtonFeatures.update_screen_update('Equipment', app))
        app.menu_edit_update_agency.triggered.connect(lambda: ButtonFeatures.update_screen_update('Agency', app))
        app.menu_edit_update_consumption.triggered.connect(lambda: ButtonFeatures.update_screen_update('Consumption', app))
        app.menu_edit_update_support.triggered.connect(lambda: ButtonFeatures.update_screen_update('Support', app))
        # ############################# #
        #              List             #
        # ############################# #

        app.menu_edit_list_client.triggered.connect(lambda: ButtonFeatures.list_screen_update('Client', app))
        app.menu_edit_list_manager.triggered.connect(lambda: ButtonFeatures.list_screen_update('Manager', app))
        app.menu_edit_list_equipment.triggered.connect(lambda: ButtonFeatures.list_screen_update('Equipment', app))
        app.menu_edit_list_agency.triggered.connect(lambda: ButtonFeatures.list_screen_update('Agency', app))
        app.menu_edit_list_consumption.triggered.connect(lambda: ButtonFeatures.list_screen_update('Consumption', app))
        app.menu_edit_list_support.triggered.connect(lambda: ButtonFeatures.list_screen_update('Support', app))
        # ############################# #
        #             Remove            #
        # ############################# #

        app.menu_edit_remove_client.triggered.connect(lambda: ButtonFeatures.remove_screen_update('Client', app))
        app.menu_edit_remove_manager.triggered.connect(lambda: ButtonFeatures.remove_screen_update('Manager', app))
        app.menu_edit_remove_equipment.triggered.connect(lambda: ButtonFeatures.remove_screen_update('Equipment', app))
        app.menu_edit_remove_agency.triggered.connect(lambda: ButtonFeatures.remove_screen_update('Agency', app))
        app.menu_edit_remove_consumption.triggered.connect(lambda: ButtonFeatures.remove_screen_update('Consumption', app))
        app.menu_edit_remove_support.triggered.connect(lambda: ButtonFeatures.remove_screen_update('Support', app))

        # ############################# #
        #          Form buttons         #
        # ############################# #
        app.btn_add.clicked.connect(lambda: ButtonFeatures.add_client(app))
        app.btn_cancel.clicked.connect(lambda: ButtonFeatures.cancel(app))


class SwitchWidget(object):
    @staticmethod
    def login2new(app):
        app.widget_login.setVisible(False)
        app.widget_add.setVisible(True)
