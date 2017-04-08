from models.crud import *


class ButtonFeatures(object):
    @staticmethod
    def log_in(app):
        SwitchWidget.to_home(app)
        # log in

    # _________________MENU BAR___________________
    @staticmethod
    def log_out(app):
        SwitchWidget.to_login(app)
        # log out

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


class ButtonListener(object):
    @staticmethod
    def action_listener(app):
        # _________________MENU BAR___________________
        app.menu_file_logout.triggered.connect(lambda: ButtonFeatures.log_out(app))
        app.menu_settings_manage.triggered.connect(lambda: SwitchWidget.to_crud(app))

        # _________________LOGIN BUTTONS_________________
        app.login_btn_login.clicked.connect(lambda: ButtonFeatures.log_in(app))
        app.btn_home.clicked.connect(lambda: SwitchWidget.to_home(app))


class SwitchWidget(object):
    @staticmethod
    def to_login(app):
        # Hide
        app.home_widget.setVisible(False)
        app.btn_home.setVisible(False)
        app.tab_crud.setVisible(False)
        app.menubar.setEnabled(False)

        # Show
        app.login_widget.setVisible(True)

    @staticmethod
    def to_crud(app):
        # Hide
        app.home_widget.setVisible(False)

        # Show
        app.tab_crud.setVisible(True)

    @staticmethod
    def to_home(app):
        # Hide
        app.login_widget.setVisible(False)
        app.tab_crud.setVisible(False)

        # Show
        app.menubar.setEnabled(True)
        app.btn_home.setVisible(True)
        app.home_widget.setVisible(True)
