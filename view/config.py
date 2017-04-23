from PyQt4 import QtGui, QtCore


class UiConfig(object):

    @staticmethod
    def config_ui(app):
        # Some last GUI configs
        UiConfig.configure_tables(app)
        UiConfig.configure_menubar(app)

        from controller.gui_listener import ButtonListener, SwitchWidget
        SwitchWidget.to_login(app)
        ButtonListener.action_listener(app)
        # Expands sidebar items
        app.sidebar.topLevelItem(0).setExpanded(True)
        app.sidebar.topLevelItem(1).setExpanded(True)
        # Validators
        # regex_cpf = QtCore.QRegExp('\d{1,3}\.\d{1,3}\.\d{1,3}\-\d{1,2}$')
        # validator_cpf = QtGui.QRegExpValidator(regex_cpf)
        # app.login_input_cpf.setValidator(validator_cpf)
        # or
        # InputMask
        app.login_input_cpf.setInputMask('999.999.999-99;')
        app.consumption_input_day.setDate(QtCore.QDate.currentDate())

    @staticmethod
    def configure_tables(app):
        # home table
        header = app.home_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        # client table
        header = app.client_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        # manager table
        header = app.manager_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        # equipment table
        header = app.equipment_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        # consumption table
        header = app.consumption_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.Stretch)
        # agency
        header = app.agency_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        # support
        header = app.support_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)

    @staticmethod
    def configure_menubar(app):
        app.menubar.setCornerWidget(app.window_buttons)
        app.btn_close.clicked.connect(lambda: app.close())
        app.btn_minimize.clicked.connect(lambda: app.showMinimized())
