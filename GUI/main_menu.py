# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from gui_listener import ButtonListener

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class UIMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("CRUD Prototype"))
        MainWindow.resize(363, 275)

        # ############################# #
        #         Central Widget        #
        # ############################# #
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # creates widget to form
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 321, 141))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))

        # creates form
        self.add_form = QtGui.QFormLayout(self.formLayoutWidget)
        self.add_form.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.add_form.setObjectName(_fromUtf8("add_form"))
        # name client
        self.lbl_form_1 = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_form_1.setObjectName(_fromUtf8("lbl_form_1"))
        self.add_form.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbl_form_1)
        self.form_input_1 = QtGui.QLineEdit(self.formLayoutWidget)
        self.form_input_1.setObjectName(_fromUtf8("form_input_1"))
        self.add_form.setWidget(1, QtGui.QFormLayout.FieldRole, self.form_input_1)
        # age client
        self.lbl_form_2 = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_form_2.setObjectName(_fromUtf8("lbl_form_2"))
        self.add_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl_form_2)
        self.form_input_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.form_input_2.setObjectName(_fromUtf8("form_input_2"))
        self.add_form.setWidget(2, QtGui.QFormLayout.FieldRole, self.form_input_2)
        # address client
        self.lbl_form_3 = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_form_3.setObjectName(_fromUtf8("lbl_form_3"))
        self.add_form.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl_form_3)
        self.form_input_3 = QtGui.QLineEdit(self.formLayoutWidget)
        self.form_input_3.setObjectName(_fromUtf8("form_input_3"))
        self.add_form.setWidget(3, QtGui.QFormLayout.FieldRole, self.form_input_3)
        # cpf client
        self.lbl_form_4 = QtGui.QLabel(self.formLayoutWidget)
        self.lbl_form_4.setObjectName(_fromUtf8("lbl_form_4"))
        self.add_form.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbl_form_4)
        self.form_input_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.form_input_4.setObjectName(_fromUtf8("form_input_4"))
        self.add_form.setWidget(4, QtGui.QFormLayout.FieldRole, self.form_input_4)

        # make form stay always on center
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.add_form.setItem(0, QtGui.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.add_form.setItem(5, QtGui.QFormLayout.FieldRole, spacerItem1)

        # ############################# #
        #          Form Buttons         #
        # ############################# #
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 321, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # cancel button
        self.btn_cancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.horizontalLayout.addWidget(self.btn_cancel)
        # align buttons
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        # create button
        self.btn_add = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.horizontalLayout.addWidget(self.btn_add)

        # ############################# #
        #          Screen Title         #
        # ############################# #

        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 321, 40))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        # Class
        self.lbl_path_class = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OpenSymbol"))
        font.setPointSize(12)
        font.setItalic(True)
        self.lbl_path_class.setFont(font)
        self.lbl_path_class.setObjectName(_fromUtf8("lbl_path_class"))
        self.horizontalLayout_2.addWidget(self.lbl_path_class)
        # separator
        self.lbl_path_arrow = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OpenSymbol"))
        font.setPointSize(12)
        self.lbl_path_arrow.setFont(font)
        self.lbl_path_arrow.setObjectName(_fromUtf8("lbl_path_arrow"))
        self.horizontalLayout_2.addWidget(self.lbl_path_arrow)
        # Method
        self.lbl_path_method = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OpenSymbol"))
        font.setPointSize(12)
        font.setItalic(True)
        self.lbl_path_method.setFont(font)
        self.lbl_path_method.setObjectName(_fromUtf8("lbl_path_method"))
        self.horizontalLayout_2.addWidget(self.lbl_path_method)
        # keeps everything aligned to left
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        # add central widget to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # ############################# #
        #            Menu Bar           #
        # ############################# #

        # creates menu bar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 363, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        # ############################# #
        #            File menu          #
        # ############################# #

        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        # File\New menu
        self.menu_file_new = QtGui.QMenu(self.menu_file)
        self.menu_file_new.setObjectName(_fromUtf8("menu_file_new"))
        # File\Import button
        self.menu_file_import = QtGui.QAction(MainWindow)
        self.menu_file_import.setObjectName(_fromUtf8("menu_file_import"))
        # File\Export button
        self.menu_file_export = QtGui.QAction(MainWindow)
        self.menu_file_export.setObjectName(_fromUtf8("menu_file_export"))
        # File\Logout button
        self.menu_file_logout = QtGui.QAction(MainWindow)
        self.menu_file_logout.setObjectName(_fromUtf8("menu_file_logout"))
        # File\Generate button
        self.menu_file_generate = QtGui.QAction(MainWindow)
        self.menu_file_generate.setObjectName(_fromUtf8("menu_file_generate"))
        # File\Quit button
        self.menu_file_quit = QtGui.QAction(MainWindow)
        self.menu_file_quit.setObjectName(_fromUtf8("menu_file_quit"))

        # File\New\Client button
        self.menu_file_new_client = QtGui.QAction(MainWindow)
        self.menu_file_new_client.setObjectName(_fromUtf8("menu_file_new_client"))
        # File\New\Manager button
        self.menu_file_new_manager = QtGui.QAction(MainWindow)
        self.menu_file_new_manager.setObjectName(_fromUtf8("menu_file_new_manager"))
        # File\New\Equipment button
        self.menu_file_new_equipment = QtGui.QAction(MainWindow)
        self.menu_file_new_equipment.setObjectName(_fromUtf8("menu_file_new_equipment"))
        # File\New\Agency button
        self.menu_file_new_agency = QtGui.QAction(MainWindow)
        self.menu_file_new_agency.setObjectName(_fromUtf8("menu_file_new_agency"))
        # File\New\Support button
        self.menu_file_new_support = QtGui.QAction(MainWindow)
        self.menu_file_new_support.setObjectName(_fromUtf8("menu_file_new_support"))
        # File\New\Consumption button
        self.menu_file_new_consumption = QtGui.QAction(MainWindow)
        self.menu_file_new_consumption.setObjectName(_fromUtf8("menu_file_new_consumption"))

        # ############################# #
        #            Edit menu          #
        # ############################# #

        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setObjectName(_fromUtf8("menu_edit"))
        # Edit\Search menu
        self.menu_edit_search = QtGui.QMenu(self.menu_edit)
        self.menu_edit_search.setObjectName(_fromUtf8("menu_edit_search"))
        # Edit\Update menu
        self.menu_edit_update = QtGui.QMenu(self.menu_edit)
        self.menu_edit_update.setObjectName(_fromUtf8("menu_edit_update"))
        # Edit\List menu
        self.menu_edit_list = QtGui.QMenu(self.menu_edit)
        self.menu_edit_list.setObjectName(_fromUtf8("menu_edit_list"))
        # Edit\Remove menu
        self.menu_edit_remove = QtGui.QMenu(self.menu_edit)
        self.menu_edit_remove.setObjectName(_fromUtf8("menu_edit_remove"))

        # Edit\Search\Client button
        self.menu_edit_search_client = QtGui.QAction(MainWindow)
        self.menu_edit_search_client.setObjectName(_fromUtf8("menu_edit_search_client"))
        # Edit\Search\Manager button
        self.menu_edit_search_manager = QtGui.QAction(MainWindow)
        self.menu_edit_search_manager.setObjectName(_fromUtf8("menu_edit_search_manager"))
        # Edit\Search\Equipment button
        self.menu_edit_search_equipment = QtGui.QAction(MainWindow)
        self.menu_edit_search_equipment.setObjectName(_fromUtf8("menu_edit_search_equipment"))
        # Edit\Search\Agency button
        self.menu_edit_search_agency = QtGui.QAction(MainWindow)
        self.menu_edit_search_agency.setObjectName(_fromUtf8("menu_edit_search_agency"))
        # Edit\Search\Consumption button
        self.menu_edit_search_consumption = QtGui.QAction(MainWindow)
        self.menu_edit_search_consumption.setObjectName(_fromUtf8("menu_edit_search_consumption"))
        # Edit\Search\Support button
        self.menu_edit_search_support = QtGui.QAction(MainWindow)
        self.menu_edit_search_support.setObjectName(_fromUtf8("menu_edit_search_support"))
        # Edit\Search\All button
        self.menu_edit_search_all = QtGui.QAction(MainWindow)
        self.menu_edit_search_all.setObjectName(_fromUtf8("menu_edit_search_all"))

        # Edit\Update\Client button
        self.menu_edit_update_client = QtGui.QAction(MainWindow)
        self.menu_edit_update_client.setObjectName(_fromUtf8("menu_edit_update_client"))
        # Edit\Update\Manager button
        self.menu_edit_update_manager = QtGui.QAction(MainWindow)
        self.menu_edit_update_manager.setObjectName(_fromUtf8("menu_edit_update_manager"))
        # Edit\Update\Equipment button
        self.menu_edit_update_equipment = QtGui.QAction(MainWindow)
        self.menu_edit_update_equipment.setObjectName(_fromUtf8("menu_edit_update_equipment"))
        # Edit\Update\Agency button
        self.menu_edit_update_agency = QtGui.QAction(MainWindow)
        self.menu_edit_update_agency.setObjectName(_fromUtf8("menu_edit_update_agency"))
        # Edit\Update\Consumption button
        self.menu_edit_update_consumption = QtGui.QAction(MainWindow)
        self.menu_edit_update_consumption.setObjectName(_fromUtf8("menu_edit_update_consumption"))
        # Edit\Update\Support button
        self.menu_edit_update_support = QtGui.QAction(MainWindow)
        self.menu_edit_update_support.setObjectName(_fromUtf8("menu_edit_update_support"))
        # Edit\Update\All button
        self.menu_edit_update_all = QtGui.QAction(MainWindow)
        self.menu_edit_update_all.setObjectName(_fromUtf8("menu_edit_update_all"))

        # Edit\List\Client button
        self.menu_edit_list_client = QtGui.QAction(MainWindow)
        self.menu_edit_list_client.setObjectName(_fromUtf8("menu_edit_list_client"))
        # Edit\List\Manager button
        self.menu_edit_list_manager = QtGui.QAction(MainWindow)
        self.menu_edit_list_manager.setObjectName(_fromUtf8("menu_edit_list_manager"))
        # Edit\List\Equipment button
        self.menu_edit_list_equipment = QtGui.QAction(MainWindow)
        self.menu_edit_list_equipment.setObjectName(_fromUtf8("menu_edit_list_equipment"))
        # Edit\List\Agency button
        self.menu_edit_list_agency = QtGui.QAction(MainWindow)
        self.menu_edit_list_agency.setObjectName(_fromUtf8("menu_edit_list_agency"))
        # Edit\List\Consumption button
        self.menu_edit_list_consumption = QtGui.QAction(MainWindow)
        self.menu_edit_list_consumption.setObjectName(_fromUtf8("menu_edit_list_consumption"))
        # Edit\List\Support button
        self.menu_edit_list_support = QtGui.QAction(MainWindow)
        self.menu_edit_list_support.setObjectName(_fromUtf8("menu_edit_list_support"))
        # Edit\List\All button
        self.menu_edit_list_all = QtGui.QAction(MainWindow)
        self.menu_edit_list_all.setObjectName(_fromUtf8("menu_edit_list_all"))

        # Edit\Remove\Client button
        self.menu_edit_remove_client = QtGui.QAction(MainWindow)
        self.menu_edit_remove_client.setObjectName(_fromUtf8("menu_edit_remove_client"))
        # Edit\Remove\Manager button
        self.menu_edit_remove_manager = QtGui.QAction(MainWindow)
        self.menu_edit_remove_manager.setObjectName(_fromUtf8("menu_edit_remove_manager"))
        # Edit\Remove\Equipment button
        self.menu_edit_remove_equipment = QtGui.QAction(MainWindow)
        self.menu_edit_remove_equipment.setObjectName(_fromUtf8("menu_edit_remove_equipment"))
        # Edit\Remove\Agency button
        self.menu_edit_remove_agency = QtGui.QAction(MainWindow)
        self.menu_edit_remove_agency.setObjectName(_fromUtf8("menu_edit_remove_agency"))
        # Edit\Remove\Consumption button
        self.menu_edit_remove_consumption = QtGui.QAction(MainWindow)
        self.menu_edit_remove_consumption.setObjectName(_fromUtf8("menu_edit_remove_consumption"))
        # Edit\Remove\Support button
        self.menu_edit_remove_support = QtGui.QAction(MainWindow)
        self.menu_edit_remove_support.setObjectName(_fromUtf8("menu_edit_remove_support"))
        # Edit\Remove\All button
        self.menu_edit_remove_all = QtGui.QAction(MainWindow)
        self.menu_edit_remove_all.setObjectName(_fromUtf8("menu_edit_remove_all"))

        # ############################# #
        #            Help menu          #
        # ############################# #
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setGeometry(QtCore.QRect(267, 128, 135, 72))
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        # Help\About button
        self.menu_help_about = QtGui.QAction(MainWindow)
        self.menu_help_about.setMenuRole(QtGui.QAction.AboutRole)
        self.menu_help_about.setObjectName(_fromUtf8("menu_help_about"))

        # Packs menu bar into main window
        MainWindow.setMenuBar(self.menubar)

        # ############################# #
        #       Menu Items Packing      #
        # ############################# #

        # File menu packing
        self.menu_file_new.addAction(self.menu_file_new_client)
        self.menu_file_new.addAction(self.menu_file_new_manager)
        self.menu_file_new.addAction(self.menu_file_new_equipment)
        self.menu_file_new.addAction(self.menu_file_new_agency)
        self.menu_file_new.addAction(self.menu_file_new_consumption)
        self.menu_file_new.addAction(self.menu_file_new_support)
        self.menu_file.addAction(self.menu_file_new.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_file_import)
        self.menu_file.addAction(self.menu_file_export)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_file_generate)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_file_logout)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_file_quit)

        # Edit menu packing
        # Edit\Search menu packing
        self.menu_edit_search.addAction(self.menu_edit_search_client)
        self.menu_edit_search.addAction(self.menu_edit_search_manager)
        self.menu_edit_search.addAction(self.menu_edit_search_equipment)
        self.menu_edit_search.addAction(self.menu_edit_search_agency)
        self.menu_edit_search.addAction(self.menu_edit_search_consumption)
        self.menu_edit_search.addAction(self.menu_edit_search_support)
        self.menu_edit_search.addSeparator()
        self.menu_edit_search.addAction(self.menu_edit_search_all)
        # Edit\Update menu packing
        self.menu_edit_update.addAction(self.menu_edit_update_client)
        self.menu_edit_update.addAction(self.menu_edit_update_manager)
        self.menu_edit_update.addAction(self.menu_edit_update_equipment)
        self.menu_edit_update.addAction(self.menu_edit_update_agency)
        self.menu_edit_update.addAction(self.menu_edit_update_consumption)
        self.menu_edit_update.addAction(self.menu_edit_update_support)
        self.menu_edit_update.addSeparator()
        self.menu_edit_update.addAction(self.menu_edit_update_all)
        # Edit\List menu packing
        self.menu_edit_list.addAction(self.menu_edit_list_client)
        self.menu_edit_list.addAction(self.menu_edit_list_manager)
        self.menu_edit_list.addAction(self.menu_edit_list_equipment)
        self.menu_edit_list.addAction(self.menu_edit_list_agency)
        self.menu_edit_list.addAction(self.menu_edit_list_consumption)
        self.menu_edit_list.addAction(self.menu_edit_list_support)
        self.menu_edit_list.addSeparator()
        self.menu_edit_list.addAction(self.menu_edit_list_all)
        # Edit\Remove menu packing
        self.menu_edit_remove.addAction(self.menu_edit_remove_client)
        self.menu_edit_remove.addAction(self.menu_edit_remove_manager)
        self.menu_edit_remove.addAction(self.menu_edit_remove_equipment)
        self.menu_edit_remove.addAction(self.menu_edit_remove_agency)
        self.menu_edit_remove.addAction(self.menu_edit_remove_consumption)
        self.menu_edit_remove.addAction(self.menu_edit_remove_support)
        self.menu_edit_remove.addSeparator()
        self.menu_edit_remove.addAction(self.menu_edit_remove_all)
        # Edit menu packing
        self.menu_edit.addAction(self.menu_edit_search.menuAction())
        self.menu_edit.addAction(self.menu_edit_update.menuAction())
        self.menu_edit.addAction(self.menu_edit_list.menuAction())
        self.menu_edit.addAction(self.menu_edit_remove.menuAction())

        # Help menu packing
        self.menu_help.addAction(self.menu_help_about)

        # MenuBar packing
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.action_listener()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CRUD Prototype", None))
        self.lbl_form_1.setText(_translate("MainWindow", "Name:", None))
        self.lbl_form_2.setText(_translate("MainWindow", "Age:", None))
        self.lbl_form_3.setText(_translate("MainWindow", "Address:", None))
        self.lbl_form_4.setText(_translate("MainWindow", "CPF:", None))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel", None))
        self.btn_add.setText(_translate("MainWindow", "Create", None))
        self.lbl_path_class.setText(_translate("MainWindow", "Client", None))
        self.lbl_path_arrow.setText(_translate("MainWindow", ">", None))
        self.lbl_path_method.setText(_translate("MainWindow", "New", None))
        self.menu_file.setTitle(_translate("MainWindow", "File", None))
        self.menu_file_new.setTitle(_translate("MainWindow", "New", None))
        self.menu_help.setTitle(_translate("MainWindow", "Help", None))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit", None))
        self.menu_edit_search.setTitle(_translate("MainWindow", "Search", None))
        self.menu_edit_update.setTitle(_translate("MainWindow", "Update", None))
        self.menu_edit_list.setTitle(_translate("MainWindow", "List", None))
        self.menu_edit_remove.setTitle(_translate("MainWindow", "Remove", None))
        self.menu_help_about.setText(_translate("MainWindow", "About", None))
        self.menu_file_new_client.setText(_translate("MainWindow", "Client", None))
        self.menu_file_new_manager.setText(_translate("MainWindow", "Manager", None))
        self.menu_file_new_equipment.setText(_translate("MainWindow", "Equipment", None))
        self.menu_file_new_agency.setText(_translate("MainWindow", "Agency", None))
        self.menu_file_new_support.setText(_translate("MainWindow", "Support", None))
        self.menu_file_new_consumption.setText(_translate("MainWindow", "Consumption", None))
        self.menu_file_import.setText(_translate("MainWindow", "Import", None))
        self.menu_file_export.setText(_translate("MainWindow", "Export", None))
        self.menu_file_logout.setText(_translate("MainWindow", "Log out", None))
        self.menu_file_generate.setText(_translate("MainWindow", "Generate report (.pdf)", None))
        self.menu_file_quit.setText(_translate("MainWindow", "Quit", None))
        self.menu_file_quit.setToolTip(_translate("MainWindow", "Quit", None))
        self.menu_edit_search_client.setText(_translate("MainWindow", "Client", None))
        self.menu_edit_search_manager.setText(_translate("MainWindow", "Manager", None))
        self.menu_edit_search_equipment.setText(_translate("MainWindow", "Equipment", None))
        self.menu_edit_search_agency.setText(_translate("MainWindow", "Agency", None))
        self.menu_edit_search_consumption.setText(_translate("MainWindow", "Consumption", None))
        self.menu_edit_search_support.setText(_translate("MainWindow", "Support", None))
        self.menu_edit_search_all.setText(_translate("MainWindow", "All", None))
        self.menu_edit_update_client.setText(_translate("MainWindow", "Client", None))
        self.menu_edit_update_manager.setText(_translate("MainWindow", "Manager", None))
        self.menu_edit_update_equipment.setText(_translate("MainWindow", "Equipment", None))
        self.menu_edit_update_agency.setText(_translate("MainWindow", "Agency", None))
        self.menu_edit_update_consumption.setText(_translate("MainWindow", "Consumption", None))
        self.menu_edit_update_support.setText(_translate("MainWindow", "Support", None))
        self.menu_edit_update_all.setText(_translate("MainWindow", "All", None))
        self.menu_edit_list_client.setText(_translate("MainWindow", "Client", None))
        self.menu_edit_list_manager.setText(_translate("MainWindow", "Manager", None))
        self.menu_edit_list_equipment.setText(_translate("MainWindow", "Equipment", None))
        self.menu_edit_list_agency.setText(_translate("MainWindow", "Agency", None))
        self.menu_edit_list_consumption.setText(_translate("MainWindow", "Consumption", None))
        self.menu_edit_list_support.setText(_translate("MainWindow", "Support", None))
        self.menu_edit_list_all.setText(_translate("MainWindow", "All", None))
        self.menu_edit_remove_client.setText(_translate("MainWindow", "Client", None))
        self.menu_edit_remove_manager.setText(_translate("MainWindow", "Manager", None))
        self.menu_edit_remove_equipment.setText(_translate("MainWindow", "Equipment", None))
        self.menu_edit_remove_agency.setText(_translate("MainWindow", "Agency", None))
        self.menu_edit_remove_consumption.setText(_translate("MainWindow", "Consumption", None))
        self.menu_edit_remove_support.setText(_translate("MainWindow", "Support", None))
        self.menu_edit_remove_all.setText(_translate("MainWindow", "All", None))

    def action_listener(self):
        # ############################# #
        #               New             #
        # ############################# #
        lbl_forms = [self.lbl_form_1, self.lbl_form_2, self.lbl_form_3, self.lbl_form_4, ]
        form_inputs = [self.form_input_1, self.form_input_2, self.form_input_3, self.form_input_4, ]
        # client
        self.menu_file_new_client.triggered.connect(lambda: ButtonListener.new_screen_update(
            str(self.menu_file_new_client.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # manager
        self.menu_file_new_manager.triggered.connect(lambda: ButtonListener.new_screen_update(
            str(self.menu_file_new_manager.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # equipment
        self.menu_file_new_equipment.triggered.connect(lambda: ButtonListener.new_screen_update(
            str(self.menu_file_new_equipment.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # agency
        self.menu_file_new_agency.triggered.connect(lambda: ButtonListener.new_screen_update(
            str(self.menu_file_new_agency.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # consumption
        self.menu_file_new_consumption.triggered.connect(lambda: ButtonListener.new_screen_update(
            str(self.menu_file_new_consumption.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # support
        self.menu_file_new_support.triggered.connect(lambda: ButtonListener.new_screen_update(
            str(self.menu_file_new_support.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # ############################# #
        #             Search            #
        # ############################# #

        # client
        self.menu_edit_search_client.triggered.connect(lambda: ButtonListener.search_screen_update(
            str(self.menu_edit_search_client.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # manager
        self.menu_edit_search_manager.triggered.connect(lambda: ButtonListener.search_screen_update(
            str(self.menu_edit_search_manager.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # equipment
        self.menu_edit_search_equipment.triggered.connect(lambda: ButtonListener.search_screen_update(
            str(self.menu_edit_search_equipment.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # agency
        self.menu_edit_search_agency.triggered.connect(lambda: ButtonListener.search_screen_update(
            str(self.menu_edit_search_agency.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # consumption
        self.menu_edit_search_consumption.triggered.connect(lambda: ButtonListener.search_screen_update(
            str(self.menu_edit_search_consumption.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # support
        self.menu_edit_search_support.triggered.connect(lambda: ButtonListener.search_screen_update(
            str(self.menu_edit_search_support.text()), self.lbl_path_class, self.lbl_path_method,
            lbl_forms, form_inputs
        ))
        # ############################# #
        #          Form buttons         #
        # ############################# #
        self.btn_add.clicked.connect(lambda: ButtonListener.add_client(
            str(self.lbl_path_class.text()), form_inputs
        ))
        self.btn_cancel.clicked.connect(lambda: ButtonListener.cancel())
