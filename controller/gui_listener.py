from PyQt4 import QtGui, QtCore
import MySQLdb
from models.crud import *
# import graph


class ButtonFeatures(object):
    @staticmethod
    def log_in(app):
        db = app.db
        cur = db.cursor()
        try:
            cur.execute("SELECT cpf, password FROM client")
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Could not fetch data from database.')
        else:
            cpf = str(app.login_input_cpf.text())
            password = str(app.login_input_password.text())
            isRegistered = False
            for (db_cpf, db_password) in cur:
                if (cpf == db_cpf) and (password == db_password):
                    # set current user
                    app.current_user = cpf
                    isRegistered = True
                    # perform login operation
                    SwitchWidget.to_home(app)
                    ClientIO.fetch_all(app)
                    break
            if not isRegistered:
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
                        ClientIO.add(name, address, cpf, age, app)
                        ClientIO.manage_password(cpf, password, app)
                        SwitchWidget.to_login(app)
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
        ButtonFeatures.clear_tables(app)
        app.sidebar.clearSelection()
        # log out

    @staticmethod
    def clear_tables(app):
        app.client_table.setRowCount(0)
        app.manager_table.setRowCount(0)
        app.equipment_table.setRowCount(0)
        app.consumption_table.setRowCount(0)
        app.agency_table.setRowCount(0)
        app.support_table.setRowCount(0)

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
        name = app.client_table.item(selected_item, 0).text()
        age = int(app.client_table.item(selected_item, 1).text())
        address = app.client_table.item(selected_item, 2).text()
        cpf = app.client_table.item(selected_item, 3).text()
        app.client_input_name.setText(name)
        app.client_input_age.setValue(age)
        app.client_input_address.setText(address)
        app.client_input_cpf.setText(cpf)

    @staticmethod
    def client_delete(app):
        selected_item = app.client_table.currentRow()
        cpf = app.client_table.item(selected_item, 3).text()
        ClientIO.delete(cpf, app)
        app.client_table.removeRow(selected_item)


class ButtonListener(object):
    @staticmethod
    def action_listener(app):

        # _________________MENU BAR______________________
        app.menu_file_logout.triggered.connect(lambda: ButtonFeatures.log_out(app))

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

        # _________________CLIENT MANAGING_______________
        app.client_btn_create.clicked.connect(lambda: ButtonFeatures.client_create(app))
        app.client_btn_edit.clicked.connect(lambda: ButtonFeatures.client_edit(app))
        app.client_btn_delete.clicked.connect(lambda: ButtonFeatures.client_delete(app))

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

        # Show
        app.login_widget.setVisible(True)

    @staticmethod
    def to_crud(app):
        # Hide
        app.home_widget.setVisible(False)

        # Show
        app.tab_crud.setVisible(True)
        app.sidebar.setVisible(True)
        app.sidebar_lbl_settings.setVisible(True)
        app.sidebar_lbl_profile.setVisible(True)

    @staticmethod
    def to_home(app):
        # Hide
        app.login_widget.setVisible(False)
        app.tab_crud.setVisible(False)

        # Show
        app.menubar.setEnabled(True)
        app.btn_home.setVisible(True)
        app.home_widget.setVisible(True)
        app.sidebar.setVisible(True)
        app.sidebar_lbl_settings.setVisible(True)
        app.sidebar_lbl_profile.setVisible(True)
