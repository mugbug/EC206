from PyQt4 import QtGui, QtCore
import MySQLdb
from models.crud import *
from models.models import *
# import graph


class ButtonFeatures(object):
    @staticmethod
    def log_in(app):
        db = app.db
        cur = db.cursor()
        try:
            cur.execute("SELECT cpf, password FROM user")
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Could not fetch data from database.')
        else:
            cpf = str(app.login_input_cpf.text())
            password = str(app.login_input_password.text())
            is_registered = False
            for (db_cpf, db_password) in cur:
                if (cpf == db_cpf) and (password == db_password):
                    # set current user
                    app.current_user = cpf
                    is_registered = True
                    # perform login operation
                    SwitchWidget.to_about(app)
                    # fetching data
                    ClientIO.fetch_all(app)
                    ManagerIO.init_comboboxes(app)
                    ManagerIO.fetch_all(app)
                    EquipmentIO.fetch_all(app)
                    AgencyIO.fetch_all(app)
                    # clearing login fields
                    app.login_input_cpf.clear()
                    app.login_input_password.clear()
                    break
            if not is_registered:
                QMessageBox.critical(app, 'Error!', 'Incorrect CPF or password!')

    # _________________REGISTER___________________
    @staticmethod
    def register(app):
        name = unicode(app.register_input_name.text()).encode('latin-1')
        age = app.register_input_age.value()
        address = unicode(app.register_input_address.text()).encode('latin-1')
        cpf = str(app.register_input_cpf.text())
        password = str(app.register_input_password.text())
        password_confirmation = str(app.register_input_password_1.text())
        if (cpf and password) != '':
            if len(cpf) == 14:
                if password_confirmation != '':
                    if password == password_confirmation:
                        already_registered = ClientIO.create_user(cpf, password, app)
                        if not already_registered:
                            ClientIO.add(name, address, cpf, age, app)
                            SwitchWidget.to_login(app)

                            app.register_input_name.clear()
                            app.register_input_age.clear()
                            app.register_input_address.clear()
                            app.register_input_cpf.clear()
                            app.register_input_password.clear()
                            app.register_input_password_1.clear()
                            app.login_input_cpf.setText(cpf)
                            app.login_input_password.setText(password)
                    else:
                        QMessageBox.critical(app, 'Error!', 'The passwords do not match!')
                else:
                    QMessageBox.critical(app, 'Error!', 'Confirm your password, please!')
            else:
                QMessageBox.critical(app, 'Error!', 'Enter a valid CPF!')
        else:
            QMessageBox.critical(app, 'Error!', 'All required fields must be filled!')

    # _________________MENU BAR___________________
    @staticmethod
    def log_out(app):
        SwitchWidget.to_login(app)
        ButtonFeatures.clear(app)
        app.sidebar.clearSelection()
        # log out

    @staticmethod
    def clear(app):
        app.client_table.setRowCount(0)
        app.manager_table.setRowCount(0)
        app.equipment_table.setRowCount(0)
        app.consumption_table.setRowCount(0)
        app.agency_table.setRowCount(0)
        app.support_table.setRowCount(0)

        app.client_input_name.clear()
        app.client_input_age.setValue(0)
        app.client_input_address.clear()
        app.client_input_cpf.clear()
        app.manager_input_cpf.clear()
        app.manager_input_agency.clear()
        app.equipment_input_name.clear()
        app.equipment_input_power.setValue(0)

    # _________________HOME_______________________
    @staticmethod
    def export_pdf(app):
        pass
    #     file_name = QtCore.QString('report.pdf')
    #
    #     printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
    #     printer.setOutputFileName(file_name)
    #     printer.setPaperSize(QtGui.QPrinter.A4)
    #     printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
    #
    #     painter = QtGui.QPainter(app)
    #     painter.setRenderHint(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing
    #                           | QtGui.QPainter.SmoothPixmapTransform)
    #     app.home_table.render(painter)
    #     painter.end()

    # _________________CLIENT MANAGER_____________
    @staticmethod
    def client_create(app):
        name = unicode(app.client_input_name.text()).encode('latin-1')
        # name = str(app.client_input_name.text().toUtf8()).encode('')
        age = app.client_input_age.value()
        address = unicode(app.client_input_address.text()).encode('latin-1')
        cpf = str(app.client_input_cpf.text())
        # if (name and address and cpf and age) != '':
        result = ClientIO.add(name, address, cpf, age, app)
        if result == 0:
            # field cleaner
            app.client_input_name.clear()
            app.client_input_age.clear()
            app.client_input_address.clear()
            app.client_input_cpf.clear()
            # add item to table
            row_position = app.client_table.rowCount()
            app.client_table.insertRow(row_position)
            app.client_table.setItem(row_position, 0, QtGui.QTableWidgetItem(name))
            app.client_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(age)))
            app.client_table.setItem(row_position, 2, QtGui.QTableWidgetItem(address))
            app.client_table.setItem(row_position, 3, QtGui.QTableWidgetItem(cpf))
        elif result == 1:
            row_position = app.client_table.currentRow()
            app.client_table.setItem(row_position, 0, QtGui.QTableWidgetItem(name))
            app.client_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(age)))
            app.client_table.setItem(row_position, 2, QtGui.QTableWidgetItem(address))
            app.client_table.setItem(row_position, 3, QtGui.QTableWidgetItem(cpf))

        # else:
        #     QtGui.QMessageBox.critical(app, 'Error!', 'All fields should be filled!')

    @staticmethod
    def client_edit(app):
        selected_item = app.client_table.currentRow()
        if selected_item != -1:
            name = app.client_table.item(selected_item, 0).text()
            age = int(app.client_table.item(selected_item, 1).text())
            address = app.client_table.item(selected_item, 2).text()
            cpf = app.client_table.item(selected_item, 3).text()
            app.client_input_name.setText(name)
            app.client_input_age.setValue(age)
            app.client_input_address.setText(address)
            app.client_input_cpf.setText(cpf)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the client to be edited!')

    @staticmethod
    def client_delete(app):
        selected_item = app.client_table.currentRow()
        if selected_item != -1:
            cpf = app.client_table.item(selected_item, 3).text()
            ClientIO.delete(cpf, app)
            app.client_table.removeRow(selected_item)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the client to be deleted!')

    # ________ MANAGER ____________
    @staticmethod
    def manager_create(app):
        cpf = app.manager_input_cpf.currentText()
        agency = app.manager_input_agency.currentText()
        result = ManagerIO.add(cpf, agency, app)
        if result == 0:
            # field cleaner
            app.manager_input_cpf.setCurrentIndex(0)
            app.manager_input_agency.setCurrentIndex(0)
            # add item to table
            row_position = app.manager_table.rowCount()
            app.manager_table.insertRow(row_position)
            app.manager_table.setItem(row_position, 0, QtGui.QTableWidgetItem(cpf))
            app.manager_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency))
        elif result == 1:
            row_position = app.manager_table.currentRow()
            app.manager_table.setItem(row_position, 0, QtGui.QTableWidgetItem(cpf))
            app.manager_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency))

    @staticmethod
    def manager_delete(app):
        selected_item = app.manager_table.currentRow()
        print selected_item
        if selected_item != -1:
            cpf = app.manager_table.item(selected_item, 0).text()
            ManagerIO.delete(cpf, app)
            app.manager_table.removeRow(selected_item)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the manager to be deleted!')

    @staticmethod
    def equipment_create(app):
        name = unicode(app.equipment_input_name.text()).encode('latin-1')
        power = app.equipment_input_power.value()
        row_position = app.equipment_table.rowCount()
        already_registered = False
        for row in range(0, row_position):
            registered_name = app.equipment_table.item(row, 0)
            if registered_name == name:
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation', 'Update {0}?'.format(registered_name),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.equipment_table.setItem(row, 1, QtGui.QTableWidgetItem(str(power)))
        if not already_registered:
            app.equipment_table.insertRow(row_position)
            app.equipment_table.setItem(row_position, 0, QtGui.QTableWidgetItem(name))
            app.equipment_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(power)))
            QMessageBox.information(app, 'Success!', 'Equipment successfully registered!')

    @staticmethod
    def equipment_edit(app):
        selected_item = app.equipment_table.currentRow()
        if selected_item != -1:
            name = app.equipment_table.item(selected_item, 0).text()
            power = int(app.equipment_table.item(selected_item, 1).text())
            app.equipment_input_name.setText(name)
            app.equipment_input_power.setValue(power)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the equipment to be edited!')

    @staticmethod
    def equipment_delete(app):
        selected_item = app.equipment_table.currentRow()
        if selected_item != -1:
            name = app.equipment_table.item(selected_item, 0).text()
            answer = QMessageBox.question(app, 'Confirmation', 'Delete {0}?'.format(name),
                                          QMessageBox.Ok | QMessageBox.Cancel)
            if answer == QMessageBox.Ok:
                app.equipment_table.removeRow(selected_item)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the equipment to be deleted!')

    @staticmethod
    def equipment_save(app):
        e = []
        table_len = app.equipment_table.rowCount()
        for row in range(0, table_len):
            name = app.equipment_table.item(row, 0).text()
            power = app.equipment_table.item(row, 1).text()
            e.append(Equipment(name, power))

        EquipmentIO.save(e, app)

    @staticmethod
    def agency_create(app):
        address = unicode(app.agency_input_address.text()).encode('latin-1')
        city = unicode(app.agency_input_city.text()).encode('latin-1')
        row_position = app.agency_table.rowCount()
        already_registered = False
        for row in range(0, row_position):
            registered_city = app.agency_table.item(row, 0)
            if registered_city == city:
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation', 'Update "{0}" agency address?'.format(registered_city),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.agency_table.setItem(row, 1, QtGui.QTableWidgetItem(address))
            registered_address = app.agency_table.item(row, 1)
            if registered_address == address:
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation', 'Update "{0}" agency city?'.format(registered_address),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.agency_table.setItem(row, 0, QtGui.QTableWidgetItem(city))
        if not already_registered:
            app.agency_table.insertRow(row_position)
            app.agency_table.setItem(row_position, 0, QtGui.QTableWidgetItem(city))
            app.agency_table.setItem(row_position, 1, QtGui.QTableWidgetItem(address))
            app.agency_table.setItem(row_position, 2, QtGui.QTableWidgetItem('-'))
            QMessageBox.information(app, 'Success!', 'Agency successfully registered!')

    @staticmethod
    def agency_edit(app):
        selected_item = app.agency_table.currentRow()
        if selected_item != -1:
            city = unicode(app.agency_table.item(selected_item, 0).text()).encode('latin-1')
            address = unicode(app.agency_table.item(selected_item, 1).text()).encode('latin-1')
            app.agency_input_city.setText(city)
            app.agency_input_address.setText(address)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the agency to be edited!')

    @staticmethod
    def agency_delete(app):
        selected_item = app.agency_table.currentRow()
        if selected_item != -1:
            city = unicode(app.agency_input_city.text()).encode('latin-1')
            answer = QMessageBox.question(app, 'Confirmation', 'Delete {0} agency?'.format(city),
                                          QMessageBox.Ok | QMessageBox.Cancel)
            if answer == QMessageBox.Ok:
                app.agency_table.removeRow(selected_item)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the agency to be deleted!')

    @staticmethod
    def agency_save(app):
        a = []
        table_len = app.agency_table.rowCount()
        for row in range(0, table_len):
            address = unicode(app.agency_input_address.text()).encode('latin-1')
            city = unicode(app.agency_input_city.text()).encode('latin-1')
            a.append(Agency(address, city))

        AgencyIO.save(a, app)


class ButtonListener(object):
    @staticmethod
    def action_listener(app):

        # _________________MENU BAR______________________
        app.menu_file_logout.triggered.connect(lambda: ButtonFeatures.log_out(app))
        app.menu_file_quit.triggered.connect(lambda: app.close())
        app.menu_help_about.triggered.connect(lambda: SwitchWidget.to_about(app))

        # _________________SIDEBAR_______________________
        app.connect(app.sidebar, QtCore.SIGNAL("itemClicked(QTreeWidgetItem*, int)"),
                    ButtonListener.sidebar_item_clicked)

        # _________________LOGIN BUTTONS_________________
        app.login_btn_login.clicked.connect(lambda: ButtonFeatures.log_in(app))
        app.login_btn_register.clicked.connect(lambda: SwitchWidget.to_register(app))

        # _________________REGISTER______________________
        app.register_btn_login.clicked.connect(lambda: SwitchWidget.to_login(app))
        app.register_btn_confirm.clicked.connect(lambda: ButtonFeatures.register(app))

        # _________________HOME__________________________
        app.home_btn_generate_report.clicked.connect(lambda: ButtonFeatures.export_pdf(app))
        app.btn_home.clicked.connect(lambda: SwitchWidget.to_about(app))

        # _________________CLIENT MANAGING_______________
        app.client_btn_create.clicked.connect(lambda: ButtonFeatures.client_create(app))
        app.client_btn_edit.clicked.connect(lambda: ButtonFeatures.client_edit(app))
        app.client_btn_delete.clicked.connect(lambda: ButtonFeatures.client_delete(app))

        # _________________MANAGER_______________________
        app.manager_btn_create.clicked.connect(lambda: ButtonFeatures.manager_create(app))
        app.manager_btn_edit.clicked.connect(lambda: ButtonFeatures.manager_edit(app))
        app.manager_btn_delete.clicked.connect(lambda: ButtonFeatures.manager_delete(app))

        # _________________EQUIPMENT MANAGING____________
        app.equipment_btn_create.clicked.connect(lambda: ButtonFeatures.equipment_create(app))
        app.equipment_btn_edit.clicked.connect(lambda: ButtonFeatures.equipment_edit(app))
        app.equipment_btn_save.clicked.connect(lambda: ButtonFeatures.equipment_save(app))
        app.equipment_btn_delete.clicked.connect(lambda: ButtonFeatures.equipment_delete(app))

        # _________________AGENCY MANAG__________________
        app.agency_btn_create.clicked.connect(lambda: ButtonFeatures.agency_create(app))
        app.agency_btn_edit.clicked.connect(lambda: ButtonFeatures.agency_edit(app))
        app.agency_btn_save.clicked.connect(lambda: ButtonFeatures.agency_save(app))
        app.agency_btn_delete.clicked.connect(lambda: ButtonFeatures.agency_delete(app))

        # ________________ ABOUT ________________________
        app.about_btn_calculate.clicked.connect(lambda: SwitchWidget.to_home(app))
        app.about_btn_register.clicked.connect(lambda: SwitchWidget.to_crud_3(app))

    @staticmethod
    def sidebar_item_clicked(item, column):
        item_clicked = item.text(column)
        if item_clicked != 'Energy Waste' and \
           item_clicked != 'Manage Data':
            app = item.parent().treeWidget().parent().parent()
            if item.parent().text(column) == 'Manage Data':
                SwitchWidget.to_crud(app)
        if item_clicked == 'Client':
            app.tab_crud.setCurrentIndex(0)
        elif item_clicked == 'Manager':
            app.tab_crud.setCurrentIndex(1)
        elif item_clicked == 'Equipment':
            app.tab_crud.setCurrentIndex(2)
        elif item_clicked == 'Consumption':
            app.tab_crud.setCurrentIndex(3)
        elif item_clicked == 'Agency':
            app.tab_crud.setCurrentIndex(4)
        elif item_clicked == 'Support':
            app.tab_crud.setCurrentIndex(5)
        elif item_clicked == 'Calculate':
            SwitchWidget.to_home(app)
        elif item_clicked == 'Histogram':
            print 'Histogram item clicked'
            # graph.main()


class SwitchWidget(object):

    @staticmethod
    def to_register(app):
        app.login_widget.setVisible(False)
        app.register_widget.setVisible(True)

    @staticmethod
    def to_login(app):
        # Hide
        app.home_widget.setVisible(False)
        app.btn_home.setVisible(False)
        app.tab_crud.setVisible(False)
        app.menubar.setEnabled(False)
        app.sidebar.setVisible(False)
        app.sidebar_lbl_settings.setVisible(False)
        app.sidebar_lbl_profile.setVisible(False)
        app.register_widget.setVisible(False)
        app.about_widget.setVisible(False)

        # Show
        app.login_widget.setVisible(True)

    @staticmethod
    def to_crud(app):
        # Hide
        app.home_widget.setVisible(False)
        app.about_widget.setVisible(False)

        # Show
        app.menubar.setEnabled(True)
        app.btn_home.setVisible(True)
        app.tab_crud.setVisible(True)
        app.sidebar.setVisible(True)
        app.sidebar_lbl_settings.setVisible(True)
        app.sidebar_lbl_profile.setVisible(True)

    @staticmethod
    def to_home(app):
        # Hide
        app.login_widget.setVisible(False)
        app.tab_crud.setVisible(False)
        app.about_widget.setVisible(False)

        # Show
        app.menubar.setEnabled(True)
        app.btn_home.setVisible(True)
        app.home_widget.setVisible(True)
        app.sidebar.setVisible(True)
        app.sidebar_lbl_settings.setVisible(True)
        app.sidebar_lbl_profile.setVisible(True)

    @staticmethod
    def to_about(app):
        # Hide
        app.login_widget.setVisible(False)
        app.tab_crud.setVisible(False)
        app.btn_home.setVisible(False)
        app.home_widget.setVisible(False)

        # Show
        app.menubar.setEnabled(True)
        app.sidebar.setVisible(True)
        app.sidebar_lbl_settings.setVisible(True)
        app.sidebar_lbl_profile.setVisible(True)
        app.about_widget.setVisible(True)

    @staticmethod
    def to_crud_3(app):
        app.tab_crud.setCurrentIndex(2)
        SwitchWidget.to_crud(app)
