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

        self.leftClick = False
        # self.menubar.mouseMoveEvent = self.mouseMoveEvent
        # self.menubar.mousePressEvent = self.mousePressEvent
        # self.menubar.mouseReleaseEvent = self.mouseReleaseEvent

    def closeEvent(self, event):
        self.db.close()

    def get_db(self):
        return self.db

    def mouseMoveEvent(self, event):
        if self.leftClick == True:
            x=event.globalX()
            y=event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x-x_w, y-y_w)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.leftClick = True
            self.offset = event.pos()

    def mouseReleaseEvent(self, event):
        self.leftClick = False

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    form = Application()
    form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    form.show()
    app.exec_()
