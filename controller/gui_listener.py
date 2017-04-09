from PyQt4 import QtGui

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
        name = str(app.client_input_name.text())
        age = app.client_input_age.value()
        address = str(app.client_input_address.text())
        cpf = str(app.client_input_cpf.text())
        if (name and address and cpf and age) != '':
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
        else:
            print 'ERROR: All fields must be filled!'

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
        ClientIO.delete(cpf)
        app.client_table.removeRow(selected_item)


class ButtonListener(object):
    @staticmethod
    def action_listener(app):
        # _________________MENU BAR______________________
        app.menu_file_logout.triggered.connect(lambda: ButtonFeatures.log_out(app))
        app.menu_settings_manage.triggered.connect(lambda: SwitchWidget.to_crud(app))

        # _________________LOGIN BUTTONS_________________
        app.login_btn_login.clicked.connect(lambda: ButtonFeatures.log_in(app))
        app.btn_home.clicked.connect(lambda: SwitchWidget.to_home(app))

        # _________________HOME__________________________
        app.home_btn_generate_report.clicked.connect(lambda: ButtonFeatures.export_pdf(app))

        # _________________CLIENT MANAGING_______________
        app.client_btn_create.clicked.connect(lambda: ButtonFeatures.client_create(app))
        app.client_btn_edit.clicked.connect(lambda: ButtonFeatures.client_edit(app))
        app.client_btn_delete.clicked.connect(lambda: ButtonFeatures.client_delete(app))


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
