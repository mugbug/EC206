from PyQt4 import QtGui, QtCore
import MySQLdb
from models.crud import *
from models.models import *
from models.histogram import *


class ButtonFeatures(object):
    @staticmethod
    def log_in(app):
        db = app.db
        cur = db.cursor()
        try:
            cur.execute("SELECT cpf, password FROM User")
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
                    ConsumptionIO.fetch_all(app)
                    SupportIO.fetch_all(app)
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
        app.agency_input_address.clear()
        app.agency_input_city.clear()
        app.support_input_id.setValue(0)
        app.support_input_phone.clear()
        app.consumption_input_kwh_price.clear()
        app.home_input_equipment.clear()

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
        cpf = str(app.client_input_cpf.currentText())
        # if (name and address and cpf and age) != '':
        result = ClientIO.add(name, address, cpf, age, app)
        if result == 0:
            # add item to table
            row_position = app.client_table.rowCount()
            app.client_table.insertRow(row_position)
            app.client_table.setItem(row_position, 0, QtGui.QTableWidgetItem(name))
            app.client_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(age)))
            app.client_table.setItem(row_position, 2, QtGui.QTableWidgetItem(address))
            app.client_table.setItem(row_position, 3, QtGui.QTableWidgetItem(cpf))
        elif result == 1:
            # update
            row_position = app.client_table.currentRow()
            app.client_table.setItem(row_position, 0, QtGui.QTableWidgetItem(name))
            app.client_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(age)))
            app.client_table.setItem(row_position, 2, QtGui.QTableWidgetItem(address))
            app.client_table.setItem(row_position, 3, QtGui.QTableWidgetItem(cpf))
        # field cleaner
        app.client_input_name.clear()
        app.client_input_age.clear()
        app.client_input_address.clear()
        app.client_input_cpf.setCurrentIndex(0)
        app.client_input_name.setFocus()

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
            cpf_index = app.client_input_cpf.findText(cpf)
            app.client_input_cpf.setCurrentIndex(cpf_index)
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
            # add item to table
            row_position = app.manager_table.rowCount()
            app.manager_table.insertRow(row_position)
            app.manager_table.setItem(row_position, 0, QtGui.QTableWidgetItem(cpf))
            app.manager_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency))
        elif result == 1:
            row_position = app.manager_table.currentRow()
            app.manager_table.setItem(row_position, 0, QtGui.QTableWidgetItem(cpf))
            app.manager_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency))
        # field cleaner
        app.manager_input_cpf.setCurrentIndex(0)
        app.manager_input_agency.setCurrentIndex(0)
        app.manager_input_cpf.setFocus()

    @staticmethod
    def manager_edit(app):
        selected_item = app.manager_table.currentRow()
        if selected_item != -1:
            cpf = app.manager_table.item(selected_item, 0).text()
            agency = app.manager_table.item(selected_item, 1).text()
            cpf_index = app.manager_input_cpf.findText(cpf)
            app.manager_input_cpf.setCurrentIndex(cpf_index)
            agency_index = app.manager_input_agency.findText(agency)
            app.manager_input_agency.setCurrentIndex(agency_index)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the manager to be edited!')

    @staticmethod
    def manager_delete(app):
        selected_item = app.manager_table.currentRow()
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
            registered_name = app.equipment_table.item(row, 0).text()
            if registered_name == name:
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation', 'Update {0}?'.format(registered_name),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.equipment_table.setItem(row, 1, QtGui.QTableWidgetItem(str(power)))
                    app.equipment_input_name.clear()
                    app.equipment_input_power.setValue(0)
                    app.equipment_input_name.setFocus()
        if not already_registered:
            app.equipment_table.insertRow(row_position)
            app.equipment_table.setItem(row_position, 0, QtGui.QTableWidgetItem(name))
            app.equipment_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(power)))
            QMessageBox.information(app, 'Success!', 'Equipment successfully registered!')
            app.equipment_input_name.clear()
            app.equipment_input_power.setValue(0)
            app.equipment_input_name.setFocus()

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
            registered_city = app.agency_table.item(row, 0).text()
            registered_address = app.agency_table.item(row, 1).text()
            if registered_city == city:
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation', 'Update "{0}" agency address?'.format(registered_city),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.agency_table.setItem(row, 1, QtGui.QTableWidgetItem(address))
                    app.agency_input_address.clear()
                    app.agency_input_city.clear()
                    app.agency_input_address.setFocus()
            elif registered_address == address:
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation', 'Update "{0}" agency city?'.format(registered_address),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.agency_table.setItem(row, 0, QtGui.QTableWidgetItem(city))
                    app.agency_input_address.clear()
                    app.agency_input_city.clear()
        if not already_registered:
            app.agency_table.insertRow(row_position)
            app.agency_table.setItem(row_position, 0, QtGui.QTableWidgetItem(city))
            app.agency_table.setItem(row_position, 1, QtGui.QTableWidgetItem(address))
            app.agency_table.setItem(row_position, 2, QtGui.QTableWidgetItem('-'))
            QMessageBox.information(app, 'Success!', 'Agency successfully registered!')
            app.agency_input_address.clear()
            app.agency_input_city.clear()
            app.agency_input_address.setFocus()

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
            city = unicode(app.agency_table.item(row, 0).text()).encode('latin-1')
            address = unicode(app.agency_table.item(row, 1).text()).encode('latin-1')
            a.append(Agency(address, city))

        AgencyIO.save(a, app)

    @staticmethod
    def consumption_create(app):
        date = app.consumption_input_day.text().split('/')
        # day = date[0]
        month = date[0]
        year = date[1]
        kwh_price = 'R$ '+str(app.consumption_input_kwh_price.value())
        row_position = app.consumption_table.rowCount()
        already_registered = False
        for row in range(0, row_position):
            r_month = app.consumption_table.item(row, 0).text()
            r_year = app.consumption_table.item(row, 1).text()
            if (r_month == month) and (r_year == year):
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation',
                                              'Update "{0}" kWh price?'.format(month+'/'+year),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.consumption_table.setItem(row, 2, QtGui.QTableWidgetItem(kwh_price))
                    app.consumption_input_kwh_price.setValue(0)
                    app.consumption_input_day.setFocus()
        if not already_registered:
            app.consumption_table.insertRow(row_position)
            # app.consumption_table.setItem(row_position, 0, QtGui.QTableWidgetItem(day))
            app.consumption_table.setItem(row_position, 0, QtGui.QTableWidgetItem(month))
            app.consumption_table.setItem(row_position, 1, QtGui.QTableWidgetItem(year))
            app.consumption_table.setItem(row_position, 2, QtGui.QTableWidgetItem(kwh_price))
            QMessageBox.information(app, 'Success!', 'Energy price successfully registered!')
            app.consumption_input_kwh_price.setValue(0)
            app.consumption_input_day.setFocus()

    @staticmethod
    def consumption_edit(app):
        selected_item = app.consumption_table.currentRow()
        if selected_item != -1:
            month = int(app.consumption_table.item(selected_item, 0).text())
            year = int(app.consumption_table.item(selected_item, 1).text())
            kwh_price = float(app.consumption_table.item(selected_item, 2).text().split(' ')[1])
            app.consumption_input_day.setDate(QtCore.QDate(year, month, 1))
            app.consumption_input_kwh_price.setValue(kwh_price)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the agency to be edited!')

    @staticmethod
    def consumption_delete(app):
        selected_item = app.consumption_table.currentRow()
        if selected_item != -1:
            month = str(app.consumption_table.item(selected_item, 0).text())
            year = str(app.consumption_table.item(selected_item, 1).text())
            date = month+'/'+year
            answer = QMessageBox.question(app, 'Confirmation', 'Delete {0} kWh price?'.format(date),
                                          QMessageBox.Ok | QMessageBox.Cancel)
            if answer == QMessageBox.Ok:
                app.consumption_table.removeRow(selected_item)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the date to be deleted!')

    @staticmethod
    def consumption_save(app):
        cm = []
        table_len = app.consumption_table.rowCount()
        for row in range(0, table_len):
            month = str(app.consumption_table.item(row, 0).text())
            year = str(app.consumption_table.item(row, 1).text())
            kwh_price = float(app.consumption_table.item(row, 2).text().split(' ')[1])
            cm.append(Consumption(None, year+'-'+month+'-01', kwh_price, None, None))
        ConsumptionIO.save(cm, app)

    @staticmethod
    def support_create(app):
        id = str(app.support_input_id.value())
        phone = app.support_input_phone.text()
        row_position = app.support_table.rowCount()
        already_registered = False
        for row in range(0, row_position):
            r_id = app.support_table.item(row, 0).text()
            if r_id == id:
                already_registered = True
                answer = QMessageBox.question(app, 'Confirmation',
                                              'Update Support #{0} phone?'.format(id),
                                              QMessageBox.Ok | QMessageBox.Cancel)
                if answer == QMessageBox.Ok:
                    app.support_table.setItem(row, 1, QtGui.QTableWidgetItem(phone))
                    app.support_input_id.setValue(0)
                    app.support_input_phone.clear()
                    app.support_input_id.setFocus()
        if not already_registered:
            app.support_table.insertRow(row_position)
            app.support_table.setItem(row_position, 0, QtGui.QTableWidgetItem(id))
            app.support_table.setItem(row_position, 1, QtGui.QTableWidgetItem(phone))
            app.support_table.setItem(row_position, 2, QtGui.QTableWidgetItem('Available'))
            QMessageBox.information(app, 'Success!', 'Support successfully registered!')
            app.support_input_id.setValue(0)
            app.support_input_phone.clear()
            app.support_input_id.setFocus()

    @staticmethod
    def support_edit(app):
        selected_item = app.support_table.currentRow()
        if selected_item != -1:
            id = app.support_table.item(selected_item, 0).text()
            phone = app.support_table.item(selected_item, 1).text()
            app.support_input_id.setValue(int(id))
            app.support_input_phone.setText(phone)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the support to be edited!')

    @staticmethod
    def support_delete(app):
        selected_item = app.support_table.currentRow()
        if selected_item != -1:
            id = app.support_table.item(selected_item, 0).text()
            answer = QMessageBox.question(app, 'Confirmation', 'Delete Support #{0}?'.format(id),
                                          QMessageBox.Ok | QMessageBox.Cancel)
            if answer == QMessageBox.Ok:
                app.support_table.removeRow(selected_item)
        else:
            QMessageBox.critical(app, 'Error!', 'Please select the support to be deleted!')

    @staticmethod
    def support_save(app):
        s = []
        table_len = app.support_table.rowCount()
        for row in range(0, table_len):
            id = int(app.support_table.item(row, 0).text())
            phone = app.support_table.item(row, 1).text()
            s.append(Support(id, phone))

        SupportIO.save(s, app)

    @staticmethod
    def insert_equipment_on_table(app):
        equipment = str(app.home_input_equipment.currentText())
        row_position = app.home_table.rowCount()
        already_on_table = False
        for row in range(0, row_position):
            r_equipment = app.home_table.item(row, 0).text()
            if equipment == r_equipment:
                already_on_table = True
                QMessageBox.critical(app, 'Error!', 'Equipment already on calculator!')
        if not already_on_table:
            app.home_table.insertRow(row_position)
            # add equipment name
            app.home_table.setItem(row_position, 0, QtGui.QTableWidgetItem(equipment))
            # add date edit
            date_edit = QtGui.QDateEdit()
            date_edit.setGeometry(QtCore.QRect(280, 40, 101, 22))
            date_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "alternate-background-color: rgb(1, 95, 61);\n"
                                    "color: rgb(0, 0, 0);")
            date_edit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
            date_edit.setMinimumDate(QtCore.QDate(2017, 1, 1))
            date_edit.setCalendarPopup(True)
            date_edit.setDisplayFormat('MM/yyyy')
            date_edit.setDate(QtCore.QDate.currentDate())
            app.home_table.setCellWidget(row_position, 3, date_edit)
            # add quant. spin box
            quant = QtGui.QSpinBox()
            quant.setStyleSheet("QSpinBox {background-color: rgb(255, 255, 255);\n"
                                "border-color: rgb(255, 255, 255);}")
            app.home_table.setCellWidget(row_position, 1, quant)
            # add daily usage spin box
            daily_usage = QtGui.QDoubleSpinBox()
            daily_usage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(255, 255, 255);")
            app.home_table.setCellWidget(row_position, 2, daily_usage)
            # disable consumption cell
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            app.home_table.setItem(row_position, 4, item)

    @staticmethod
    def remove_row(app):
        selected_item = app.home_table.currentRow()
        print selected_item
        if selected_item != -1:
            app.home_table.removeRow(selected_item)

    @staticmethod
    def update_calculator(app):
        # init graph variables
        data = {}
        total = 0

        rows = app.home_table.rowCount()
        for row in range(0, rows):
            equipment_name = app.home_table.item(row, 0).text()
            power = EquipmentIO.get_equipment_power(equipment_name, app)
            date = app.home_table.cellWidget(row, 3).text().split('/')
            day = '01'
            month = date[0]
            year = date[1]
            date = year+'-'+month+'-'+day
            kwh_price = ConsumptionIO.get_kwh_price(date, app)
            quant = app.home_table.cellWidget(row, 1).value()
            daily_usage = app.home_table.cellWidget(row, 2).value()
            if (power >= 0) and (kwh_price >= 0):
                consumption = Consumption(power, day, kwh_price, daily_usage, quant)
                consumption.calculate_consumption()
                item = QtGui.QTableWidgetItem('R$ '+str(consumption.total_cost))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                app.home_table.setItem(row, 4, item)

                # add to dict
                data[equipment_name] = consumption.total_cost
                # sum cost
                total += consumption.total_consumption

        # update histogram
        PlotBarChart.plot(app, data)
        # update total cost
        app.home_input_total.display(total)


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
        app.btn_home.clicked.connect(lambda: SwitchWidget.to_about(app))
        app.home_btn_equipment.clicked.connect(lambda: ButtonFeatures.insert_equipment_on_table(app))
        app.home_btn_generate_report.clicked.connect(lambda: ButtonFeatures.export_pdf(app))

        #table
        app.remove_Action.triggered.connect(lambda: ButtonFeatures.remove_row(app))
        app.home_table_update.clicked.connect(lambda: ButtonFeatures.update_calculator(app))

        # ____________________HISTOGRM___________________--
        # app.histogram_plot.clicked.connect(lambda: ButtonFeatures.plot(app))
        # app.histogram_bnt_plot.clicked.connect(lambda: PlotBarChart.plot(app))

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

        # _________________CONSUMPTION __________________
        app.consumption_btn_create.clicked.connect(lambda: ButtonFeatures.consumption_create(app))
        app.consumption_btn_edit.clicked.connect(lambda: ButtonFeatures.consumption_edit(app))
        app.consumption_btn_save.clicked.connect(lambda: ButtonFeatures.consumption_save(app))
        app.consumption_btn_delete.clicked.connect(lambda: ButtonFeatures.consumption_delete(app))

        # _________________ SUPPORT ______________________-
        app.support_btn_create.clicked.connect(lambda: ButtonFeatures.support_create(app))
        app.support_btn_edit.clicked.connect(lambda: ButtonFeatures.support_edit(app))
        app.support_btn_save.clicked.connect(lambda: ButtonFeatures.support_save(app))
        app.support_btn_delete.clicked.connect(lambda: ButtonFeatures.support_delete(app))

        # ________________ ABOUT ________________________
        app.about_btn_calculate.clicked.connect(lambda: SwitchWidget.to_home(app))
        app.about_btn_register.clicked.connect(lambda: SwitchWidget.to_crud_3(app))
        app.about_btn_analyse.clicked.connect(lambda: SwitchWidget.to_histogram(app))

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
            SwitchWidget.to_histogram(app)


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
        app.menu_file.setEnabled(False)
        app.menu_help.setEnabled(False)
        app.sidebar.setVisible(False)
        app.register_widget.setVisible(False)
        app.about_widget.setVisible(False)
        app.histogram_widget.setVisible(False)

        # Show
        app.window_buttons.setEnabled(True)
        app.login_widget.setVisible(True)

    @staticmethod
    def to_crud(app):
        # Hide
        app.home_widget.setVisible(False)
        app.about_widget.setVisible(False)
        app.histogram_widget.setVisible(False)

        # Show
        app.menu_file.setEnabled(True)
        app.menu_help.setEnabled(True)
        app.btn_home.setVisible(True)
        app.tab_crud.setVisible(True)
        app.sidebar.setVisible(True)

    @staticmethod
    def to_home(app):
        # Hide
        app.login_widget.setVisible(False)
        app.tab_crud.setVisible(False)
        app.about_widget.setVisible(False)
        app.histogram_widget.setVisible(False)

        # Show
        app.menu_file.setEnabled(True)
        app.menu_help.setEnabled(True)
        app.btn_home.setVisible(True)
        app.home_widget.setVisible(True)
        app.sidebar.setVisible(True)

    @staticmethod
    def to_about(app):
        # Hide
        app.login_widget.setVisible(False)
        app.tab_crud.setVisible(False)
        app.btn_home.setVisible(False)
        app.home_widget.setVisible(False)
        app.histogram_widget.setVisible(False)

        # Show
        app.menu_file.setEnabled(True)
        app.menu_help.setEnabled(True)
        app.sidebar.setVisible(True)
        app.about_widget.setVisible(True)

    @staticmethod
    def to_crud_3(app):
        app.tab_crud.setCurrentIndex(2)
        SwitchWidget.to_crud(app)

    @staticmethod
    def to_histogram(app):
        # Hide
        app.login_widget.setVisible(False)
        app.tab_crud.setVisible(False)
        app.home_widget.setVisible(False)
        app.about_widget.setVisible(False)

        # Show
        app.btn_home.setVisible(True)
        app.menu_file.setEnabled(True)
        app.menu_help.setEnabled(True)
        app.sidebar.setVisible(True)
        app.histogram_widget.setVisible(True)