# coding: UTF-8
import MySQLdb
from PyQt4.QtGui import QMessageBox
from PyQt4 import QtGui, QtCore

from models import *

c = []
m = []
e = []
cm = []
a = []
s = []


class ClientIO(object):

    @staticmethod
    def add(name, address, cpf, age, app):
        """Creates new object of Client"""

        db = app.db
        cur = db.cursor()

        # client = Client(name, address, cpf, age)
        try:
            cur.execute("INSERT INTO Client (name, address, cpf, age)"
                        "VALUES ('{0}', '{1}', '{2}', {3})"
                        .format(name, address, cpf, age))
            db.commit()
        except MySQLdb.Error:
            db.rollback()
            try:
                cur.execute("SELECT cpf FROM Client WHERE cpf = ('{0}')"
                            .format(cpf))
                cpf_db = cur.fetchone()
                if cpf_db is not None:
                    answer = QMessageBox.question(app, 'Confirmation',
                                                  'Update Client data?',
                                                  QMessageBox.Ok | QMessageBox.Cancel)
                    if answer == QMessageBox.Ok:
                        ClientIO.update(name, address, cpf, age, app)
                        return 1
                else:
                    QMessageBox.critical(app, 'Error!', 'CPF not registered!')
                    return -1
            except MySQLdb.Error:
                QMessageBox.critical(app, 'Error!', 'CPF not registered!')
                return -1
        else:
            QMessageBox.information(app, 'Success!', 'Client successfully created!')
            return 0
        finally:
            cur.close()

    @staticmethod
    def create_user(cpf, password, app):
        db = app.db
        cur = db.cursor()

        try:
            cur.execute("INSERT INTO User (cpf, password) VALUES ('{0}', '{1}')".format(cpf, password))
            return 0
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'CPF already registered!')
            return 1

    @staticmethod
    def manage_password(cpf, password, app):

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("UPDATE User SET password = ('{0}') WHERE cpf = ('{1}')".format(password, cpf))
            db.commit()
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Could not update Client password!')
        finally:
            cur.close()

    @staticmethod
    def update(name, address, cpf, age, app):
        """Lets user change some Client objects attributes"""

        db = app.db
        cur = db.cursor()
        try:
            cur.execute("SELECT * FROM Client WHERE cpf = ('{0}')".format(cpf))
            client = cur.fetchone()
            client_id = client[0]
            if name != '':
                cur.execute("UPDATE Client SET name = ('{0}') WHERE idClient = ({1})".format(name, client_id))
            if address != '':
                cur.execute("UPDATE Client SET address = ('{0}') WHERE idClient = ({1})".format(address, client_id))
            # cur.execute("UPDATE client SET cpf = ('{0}') WHERE idClient = ({1})".format(cpf, client_id))
            if age != 0:
                cur.execute("UPDATE Client SET age = ({0}) WHERE idClient = ({1})".format(age, client_id))
            db.commit()
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Could not update Client!')
        else:
            QMessageBox.information(app, 'Success!', 'Client successfully updated!')
        finally:
            cur.close()

    @staticmethod
    def delete(cpf, app):
        """Removes the Client object from database"""

        db = app.db
        cur = db.cursor()
        try:
            cur.execute("DELETE FROM Client WHERE cpf = '{0}'".format(cpf))
            cur.execute("DELETE FROM User WHERE cpf = '{0}'".format(cpf))
            db.commit()
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Could not delete Client!')
        else:
            QMessageBox.information(app, 'Success!', 'Client successfully removed!')
        finally:
            cur.close()

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Client table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM Client")
            clients = cur.fetchall()

            for client in clients:
                row_position = app.client_table.rowCount()
                app.client_table.insertRow(row_position)
                app.client_table.setItem(row_position, 0, QtGui.QTableWidgetItem(client[1]))
                app.client_input_cpf.addItem(client[4])
                app.client_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(client[3])))
                app.client_table.setItem(row_position, 2, QtGui.QTableWidgetItem(client[2]))
                app.client_table.setItem(row_position, 3, QtGui.QTableWidgetItem(client[4]))
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Client data from database')
        finally:
            cur.close()


class ManagerIO(object):
    @staticmethod
    def add(cpf, agency, app):
        """Creates new object of Client"""

        db = app.db
        cur = db.cursor()

        # manager = Manager(cpf, agency)
        try:
            cur.execute("SELECT idAgency FROM Agency WHERE city = ('{0}')".format(agency))
            agency_id = cur.fetchone()
            if agency_id is not None:
                cur.execute("INSERT INTO Manager (cpf) VALUES ('{0}')")
                cur.execute("INSERT INTO Agency_has_Manager (Agency_idAgency, Manager_cpf) "
                            "VALUES ({0}, '{1}')"
                            .format(agency_id[0], cpf))
                db.commit()
        except MySQLdb.Error as err:
            # print err
            db.rollback()
            try:
                cur.execute("SELECT Manager.cpf FROM Manager WHERE cpf = ('{0}')".format(cpf))
                manager_id = cur.fetchone()
                if manager_id is not None:
                    answer = QMessageBox.question(app, 'Confirmation', 'Update manager data?',
                                                  QMessageBox.Ok | QMessageBox.Cancel)
                    if answer == QMessageBox.Ok:
                        ManagerIO.update(cpf, agency_id, app)
                        return 1
                else:
                    QMessageBox.critical(app, 'Error!', 'CPF not registered!')
                    return -1
            except MySQLdb.Error as err:
                # print err
                QMessageBox.critical(app, 'Error!', 'CPF not registered!')
                return -1
        else:
            QMessageBox.information(app, 'Success!', 'Manager successfully created!')
            return 0
        finally:
            cur.close()

    @staticmethod
    def update(cpf, agency, app):
        """Lets user change some Manager object attributes"""

        db = app.db
        cur = db.cursor()
        try:
            cpfs = []
            agencies = []
            # get current items from manager_table
            rows = app.manager_table.rowCount()
            for row in range(0,rows):
                cpfs.append(str(app.manager_table.item(row, 0).text()))
                city = str(app.manager_table.item(row, 1).text())
                cur.execute("SELECT idAgency FROM Agency WHERE city = '{0}'".format(city))
                agencies.append(cur.fetchone()[0])

            # select all items on agency_has_manager
            cur.execute("SELECT * FROM Agency_has_Manager")
            agency_manager = cur.fetchall()
            # compare both lists
            items = app.manager_table.rowCount()
            
            for item in range(items):
                agency_db = agency_manager[item][0]
                cpf_db = agency_manager[item][1]
                # if diff, update
                # once both lists must be in same order, this 'if' is valid:
                if cpf_db != cpfs[item]:
                    script = "UPDATE Agency_has_Manager SET Manager_cpf = '{0}' WHERE Agency_idAgency = {1}".format(cpf, agency_db)
                    cur.execute(script)
                if agency_db != agencies[item]:
                    script = "UPDATE Agency_has_Manager SET Agency_idAgency = {0} WHERE Manager_cpf = '{1}'".format(agency, cpf_db)
                    cur.execute(script)
                db.commit()
        except MySQLdb.Error as err:
            print err
            QMessageBox.critical(app, 'Error!', 'Could not update Manager!')
        else:
            QMessageBox.information(app, 'Success!', 'Manager successfully updated!')
        finally:
            cur.close()

    @staticmethod
    def delete(cpf, app):
        """Removes the Manager object from database"""

        db = app.db
        cur = db.cursor()
        try:
            cur.execute("DELETE FROM Manager WHERE cpf = '{0}'".format(cpf))
            db.commit()
        except MySQLdb.Error as err:
            # print err
            QMessageBox.critical(app, 'Error!', 'Could not delete Manager!')
        else:
            QMessageBox.information(app, 'Success!', 'Manager successfully removed!')
        finally:
            cur.close()

    @staticmethod
    def init_comboboxes(app):

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT cpf FROM User")
            users = cur.fetchall()
            for user in users:
                app.manager_input_cpf.addItem(user[0])

            cur.execute("SELECT city FROM Agency")
            agencies = cur.fetchall()
            for agency in agencies:
                app.manager_input_agency.addItem(agency[0])

        except MySQLdb.Error as err:
            print 'Unable to initialize Manager comboboxes!\n{0}'.format(err)
        finally:
            cur.close()

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Agency_has_Manager table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT Manager_cpf, Agency.city FROM Agency_has_Manager "
                        "INNER JOIN Agency ON Agency_idAgency = Agency.idAgency")
            agencies_managers = cur.fetchall()
            for agency_manager in agencies_managers:
                row_position = app.manager_table.rowCount()
                app.manager_table.insertRow(row_position)
                app.manager_table.setItem(row_position, 0, QtGui.QTableWidgetItem(agency_manager[0]))
                app.manager_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency_manager[1]))
        except MySQLdb.Error as err:
            print 'Unable to fetch Manager data from database\n{0}'.format(err)
        finally:
            cur.close()


class EquipmentIO(object):

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Equipment table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM Equipment WHERE User_cpf = ('{0}')".format(app.current_user))
            equipments = cur.fetchall()

            for equipment in equipments:
                # e.append(Equipment(equipment[1], equipment[2]))
                row_position = app.equipment_table.rowCount()
                app.equipment_table.insertRow(row_position)
                app.equipment_table.setItem(row_position, 0, QtGui.QTableWidgetItem(equipment[1]))
                app.equipment_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(equipment[2])))
                app.home_input_equipment.addItem(equipment[1])
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Equipment data from database')
        finally:
            cur.close()

    @staticmethod
    def save(equipments, app):
        """Saves all changes to database"""

        db = app.db
        cur = db.cursor()

        success = False

        # start update calculate screen
        app.home_input_equipment.clear()

        if len(equipments) == 0:
            try:
                cur.execute("DELETE FROM Equipment WHERE User_cpf = ('{0}')".format(app.current_user))
                db.commit()
            except MySQLdb.Error as err:
                db.rollback()
                print err
                QMessageBox.critical(app, 'Error!', 'Could not erase all Equipments.')
            else:
                success = True

        for equipment in equipments:
            try:
                cur.execute("SELECT * FROM Equipment WHERE (name, User_cpf) = ('{0}', '{1}')"
                            .format(equipment.name, app.current_user))
                result = cur.fetchone()
                if result is not None:
                    cur.execute("UPDATE Equipment SET name = ('{0}') WHERE idEquipment = ({1})"
                                .format(equipment.name, result[0]))
                    cur.execute("UPDATE Equipment SET power = ({0}) WHERE idEquipment = ({1})"
                                .format(equipment.power, result[0]))
                else:
                    cur.execute("INSERT INTO Equipment (name, power, User_cpf) VALUES ('{0}', {1}, '{2}')"
                                .format(equipment.name, equipment.power, app.current_user))
                db.commit()
            except MySQLdb.Error as err:
                db.rollback()
                print err
                QMessageBox.critical(app, 'Error!', 'Could not save changes on Equipments.')
            else:
                success = True
                # add to calculate screen
                app.home_input_equipment.addItem(equipment.name)

        if success:
            QMessageBox.information(app, 'Success!', 'Changes on Equipments successfully saved!')

    @staticmethod
    def get_equipment_power(name, app):
        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT power FROM Equipment WHERE name = '{0}'".format(name))
            power = cur.fetchone()[0]
        except MySQLdb.Error as err:
            print err
            return -1
        else:
            return power


class AgencyIO(object):

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Agency table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM Agency ")
            agencies = cur.fetchall()
            for agency in agencies:
                a.append(Agency(agency[1], agency[2]))
                row_position = app.agency_table.rowCount()
                app.agency_table.insertRow(row_position)
                app.agency_table.setItem(row_position, 0, QtGui.QTableWidgetItem(agency[2]))
                app.agency_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency[1]))
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Agency data from database')
        finally:
            cur.close()

    @staticmethod
    def save(agencies, app):
        """Saves all changes to database"""

        db = app.db
        cur = db.cursor()

        app.manager_input_agency.clear()
        success = False

        if len(agencies) == 0:
            try:
                cur.execute("DELETE FROM Agency")
                db.commit()
            except MySQLdb.Error:
                db.rollback()
                QMessageBox.critical(app, 'Error!', 'Could not erase all Agencies.')
            else:
                success = True

        for agency in agencies:
            try:
                cur.execute("SELECT * FROM Agency WHERE (address, city) = ('{0}', '{1}')"
                            .format(agency.address, agency.city))
                agency_id = cur.fetchone()
                if agency_id is not None:
                    cur.execute("UPDATE Agency SET address = ('{0}') WHERE idAgency = ({1})"
                                .format(agency.address, agency_id[0]))
                    cur.execute("UPDATE Agency SET city = ('{0}') WHERE idAgency = ({1})"
                                .format(agency.city, agency_id[0]))
                else:
                    cur.execute("INSERT INTO Agency (address, city) VALUES ('{0}', '{1}')"
                                .format(agency.address, agency.city))
                app.manager_input_agency.addItem(agency.city)
                db.commit()
            except MySQLdb.Error as err:
                db.rollback()
                print err
                QMessageBox.critical(app, 'Error!', 'Could not save changes on Agencies.')
            else:
                success = True

        if success:
            QMessageBox.information(app, 'Success!', 'Changes on Agencies successfully saved!')


class ConsumptionIO(object):

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Consumption table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM Consumption WHERE User_cpf = ('{0}')".format(app.current_user))
            consumptions = cur.fetchall()

            for consumption in consumptions:
                date = str(consumption[1]).split('-')
                year = date[0]
                month = date[1]
                # day = date[2]
                cm.append(Consumption(None, str(consumption[1]), consumption[2], None, None))
                row_position = app.consumption_table.rowCount()
                app.consumption_table.insertRow(row_position)
                # app.consumption_table.setItem(row_position, 0, QtGui.QTableWidgetItem(day))
                app.consumption_table.setItem(row_position, 0, QtGui.QTableWidgetItem(month))
                app.consumption_table.setItem(row_position, 1, QtGui.QTableWidgetItem(year))
                app.consumption_table.setItem(row_position, 2, QtGui.QTableWidgetItem('R$ '+str(consumption[2])))
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Consumption data from database')
        finally:
            cur.close()

    @staticmethod
    def save(consumptions, app):
        """Saves all changes to database"""

        db = app.db
        cur = db.cursor()

        success = False

        if len(consumptions) == 0:
            try:
                cur.execute("DELETE FROM Consumption WHERE User_cpf = ('{0}')".format(app.current_user))
                db.commit()
            except MySQLdb.Error:
                db.rollback()
                QMessageBox.critical(app, 'Error!', 'Could not erase all Consumptions.')
            else:
                success = True

        for consumption in consumptions:
            try:
                cur.execute("SELECT * FROM Consumption WHERE (day, CAST(kwh_price AS DECIMAL), User_cpf) = "
                            "('{0}', CAST({1} AS DECIMAL), '{2}')"
                            .format(consumption.day, consumption.kwh_price, app.current_user))
                consumption_id = cur.fetchone()
                if consumption_id is not None:
                    cur.execute("UPDATE Consumption SET day = ('{0}') WHERE idConsumption = ({1})"
                                .format(consumption.day, consumption_id[0]))
                    cur.execute("UPDATE Consumption SET kwh_price = ({0}) WHERE idConsumption = ({1})"
                                .format(consumption.kwh_price, consumption_id[0]))
                else:
                    cur.execute("INSERT INTO Consumption (day, kwh_price, User_cpf) VALUES ('{0}', {1}, '{2}')"
                                .format(consumption.day, consumption.kwh_price, app.current_user))
                db.commit()
            except MySQLdb.Error as err:
                db.rollback()
                print err
                QMessageBox.critical(app, 'Error!', 'Could not save changes on Consumption.')
            else:
                success = True

        if success:
            QMessageBox.information(app, 'Success!', 'Changes on Consumption successfully saved!')

    @staticmethod
    def get_kwh_price(day, app):

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT kwh_price FROM Consumption WHERE day = '{0}'".format(day))
            kwh_price = cur.fetchone()
            if kwh_price is not None:
                kwh_price = kwh_price[0]
            else:
                date = day.split('-')
                year = date[0]
                month = QtCore.QDate.longMonthName(int(date[1]))
                QMessageBox.critical(app, 'Error!', 'There is no kWh price registered for {0}, {1}'.format(month, year))
        except MySQLdb.Error as err:
            print err
            return -1
        else:
            return kwh_price


class SupportIO(object):

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Support table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM Support")
            supports = cur.fetchall()

            for support in supports:
                # s.append(Support(support[1], support[2]))
                row_position = app.support_table.rowCount()
                app.support_table.insertRow(row_position)
                app.support_table.setItem(row_position, 0, QtGui.QTableWidgetItem(str(support[0])))
                app.support_table.setItem(row_position, 1, QtGui.QTableWidgetItem(support[2]))
                if support[1]:
                    app.support_table.setItem(row_position, 2, QtGui.QTableWidgetItem('Available'))
                else:
                    app.support_table.setItem(row_position, 2, QtGui.QTableWidgetItem('Not Available'))
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Support data from database')
        finally:
            cur.close()

    @staticmethod
    def save(supports, app):
        """Saves all changes to database"""

        db = app.db
        cur = db.cursor()

        success = False
        if len(supports) == 0:
            try:
                cur.execute("DELETE FROM Support")
                db.commit()
            except MySQLdb.Error:
                db.rollback()
                QMessageBox.critical(app, 'Error!', 'Could not erase all Supports.')
            else:
                success = True

        for support in supports:
            try:
                # check if it's registered
                cur.execute("SELECT * FROM Support WHERE phone = ('{0}')"
                            .format(support.phone))
                support_id = cur.fetchone()
                if support_id is not None:
                    cur.execute("UPDATE Support SET phone = ('{0}') WHERE idSupport = ({1})"
                                .format(support.phone, support.id_number))
                else:
                    cur.execute("INSERT INTO Support (idSupport, phone) VALUES ({0}, '{1}')"
                                .format(support.id_number, support.phone))
                db.commit()
            except MySQLdb.Error as err:
                db.rollback()
                print err
                QMessageBox.critical(app, 'Error!', 'Could not save changes on Supports.')
            else:
                success = True

        if success:
            QMessageBox.information(app, 'Success!', 'Changes on Agencies successfully saved!')
