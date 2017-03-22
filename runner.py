# coding: UTF-8
import sys
from view.main_menu import UIMainWindow
from PyQt4 import QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    main_window = QtGui.QMainWindow()
    ui = UIMainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
