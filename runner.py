# coding: UTF-8
import sys
from PyQt4 import QtGui

import view.design as ui
from controller.gui_listener import ButtonListener


class Application(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)
        self.widget_add.setVisible(False)
        ButtonListener.action_listener(self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    form = Application()
    form.show()
    app.exec_()
