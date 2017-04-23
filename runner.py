# coding: UTF-8
# UI icons from https://icons8.com/
import sys
from PyQt4 import QtGui, QtCore

import view.design as ui
from view.config import UiConfig
from controller.connector import DataBaseConnector


class Application(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.current_user = str
        self.setupUi(self)
        UiConfig.config_ui(self)
        self.db = DataBaseConnector.get_db(self)

    def closeEvent(self, event):
        self.db.close()

    def get_db(self):
        return self.db


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    # import style
    # app.setStyleSheet(style.style)
    form = Application()
    form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    form.show()
    app.exec_()
