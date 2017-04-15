# coding: UTF-8
import sys
from PyQt4 import QtGui, QtCore

import view.design as ui
from controller.connector import DataBaseConnector


class Application(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)
        self.config_ui()
        self.db = DataBaseConnector.get_db(self)

    def closeEvent(self, event):
        self.db.close()

    def get_db(self):
        return self.db

    def config_ui(self):
        # Some last GUI configs
        self.configure_tables()
        from controller.gui_listener import ButtonListener, SwitchWidget
        SwitchWidget.to_login(self)
        ButtonListener.action_listener(self)
        # Expands sidebar items
        self.sidebar.topLevelItem(0).setExpanded(True)
        self.sidebar.topLevelItem(1).setExpanded(True)
        # Validators
        # regex_cpf = QtCore.QRegExp('\d{1,3}\.\d{1,3}\.\d{1,3}\-\d{1,2}$')
        # validator_cpf = QtGui.QRegExpValidator(regex_cpf)
        # self.login_input_cpf.setValidator(validator_cpf)
        # or
        # InputMask
        self.login_input_cpf.setInputMask('999.999.999-99;')

    def configure_tables(self):
        # home table
        header = self.home_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        # client table
        header = self.client_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        # manager table
        header = self.client_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        # equipment table
        header = self.equipment_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    # import style
    # app.setStyleSheet(style.style)
    form = Application()
    form.show()
    app.exec_()
