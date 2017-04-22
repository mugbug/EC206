# coding: UTF-8
import MySQLdb
from PyQt4.QtGui import QMessageBox
from PyQt4 import QtGui
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
            cur.execute("INSERT INTO client (name, address, cpf, age) VALUES ('{0}', '{1}', '{2}', {3})"
                        .format(name, address, cpf, age))
            db.commit()
        except MySQLdb.Error:
            db.rollback()
            try:
                cur.execute("SELECT cpf FROM client WHERE cpf = ('{0}')".format(cpf))
                cpf_db = cur.fetchone()
                if cpf_db is not None:
                    answer = QMessageBox.question(app, 'Confirmation', 'Update client data?',
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
            cur.execute("INSERT INTO user (cpf, password) VALUES ('{0}', '{1}')".format(cpf, password))
            return 0
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'CPF already registered!')
            return 1

    @staticmethod
    def manage_password(cpf, password, app):

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("UPDATE user SET password = ('{0}') WHERE cpf = ('{1}')".format(password, cpf))
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
            cur.execute("SELECT * FROM client WHERE cpf = ('{0}')".format(cpf))
            client = cur.fetchone()
            client_id = client[0]
            if name != '':
                cur.execute("UPDATE client SET name = ('{0}') WHERE idClient = ({1})".format(name, client_id))
            if address != '':
                cur.execute("UPDATE client SET address = ('{0}') WHERE idClient = ({1})".format(address, client_id))
            # cur.execute("UPDATE client SET cpf = ('{0}') WHERE idClient = ({1})".format(cpf, client_id))
            if age != 0:
                cur.execute("UPDATE client SET age = ({0}) WHERE idClient = ({1})".format(age, client_id))
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
            cur.execute("DELETE FROM client WHERE cpf = '{0}'".format(cpf))
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
            cur.execute("SELECT * FROM client")
            clients = cur.fetchall()

            for client in clients:
                row_position = app.client_table.rowCount()
                app.client_table.insertRow(row_position)
                app.client_table.setItem(row_position, 0, QtGui.QTableWidgetItem(client[1]))
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
            cur.execute("SELECT idAgency FROM agency WHERE city = ('{0}')".format(agency))
            agency_id = cur.fetchone()
            cur.execute("INSERT INTO manager (Agency_idAgency, cpf) VALUES ({0}, '{1}')"
                        .format(agency_id[0], cpf))
            db.commit()
        except MySQLdb.Error as err:
            print err
            db.rollback()
            try:
                cur.execute("SELECT idManager FROM manager WHERE cpf = ('{0}')".format(cpf))
                manager_id = cur.fetchone()
                if manager_id is not None:
                    answer = QMessageBox.question(app, 'Confirmation', 'Update manager data?',
                                                  QMessageBox.Ok | QMessageBox.Cancel)
                    if answer == QMessageBox.Ok:
                        ManagerIO.update(cpf, agency, app)
                        return 1
                else:
                    QMessageBox.critical(app, 'Error!', 'CPF not registered!')
                    return -1
            except MySQLdb.Error as err:
                print err
                QMessageBox.critical(app, 'Error!', 'CPF not registered!')
                return -1
        else:
            QMessageBox.information(app, 'Success!', 'Manager successfully created!')
            return 0
        finally:
            cur.close()

    @staticmethod
    def update(cpf, agency, app):
        """Lets user change some Client objects attributes"""

        db = app.db
        cur = db.cursor()
        try:
            cur.execute("SELECT idAgency FROM agency WHERE city = ('{0}')".format(agency))
            agency_id = cur.fetchone()[0]
            cur.execute("SELECT * FROM manager WHERE cpf = ('{0}')".format(cpf))
            manager = cur.fetchone()
            manager_id = manager[0]
            if cpf != '':
                cur.execute("UPDATE manager SET cpf = ('{0}') WHERE idManager = ({1})".format(cpf, manager_id))
            if agency != '':
                cur.execute("UPDATE manager SET agency = ({0}) WHERE idManager = ({1})".format(agency_id, manager_id))
            db.commit()
        except MySQLdb.Error:
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
            cur.execute("DELETE FROM manager WHERE cpf = '{0}'".format(cpf))
            db.commit()
        except MySQLdb.Error:
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
            cur.execute("SELECT cpf FROM user")
            users = cur.fetchall()
            for user in users:
                app.manager_input_cpf.addItem(user[0])

            cur.execute("SELECT city FROM agency")
            agencies = cur.fetchall()
            for agency in agencies:
                app.manager_input_agency.addItem(agency[0])

        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to initialize Manager comboboxes!')
        finally:
            cur.close()

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Manager table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM manager")
            managers = cur.fetchall()
            for manager in managers:
                row_position = app.manager_table.rowCount()
                app.manager_table.insertRow(row_position)
                app.manager_table.setItem(row_position, 0, QtGui.QTableWidgetItem(manager[2]))
                cur.execute("SELECT city FROM agency WHERE idAgency = ({0})".format(manager[1]))
                city = cur.fetchone()
                app.manager_table.setItem(row_position, 1, QtGui.QTableWidgetItem(city[0]))
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Manager data from database')
        finally:
            cur.close()


class EquipmentIO(object):

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Equipment table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM equipment WHERE User_cpf = ('{0}')".format(app.current_user))
            equipments = cur.fetchall()

            for equipment in equipments:
                e.append(Equipment(equipment[1], equipment[2]))
                row_position = app.equipment_table.rowCount()
                app.equipment_table.insertRow(row_position)
                app.equipment_table.setItem(row_position, 0, QtGui.QTableWidgetItem(equipment[1]))
                app.equipment_table.setItem(row_position, 1, QtGui.QTableWidgetItem(str(equipment[2])))
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
        for equipment in equipments:
            try:
                cur.execute("SELECT * FROM equipment WHERE (name, User_cpf) = ('{0}', '{1}')"
                            .format(equipment.name, app.current_user))
                result = cur.fetchone()
                if result is not None:
                    cur.execute("UPDATE equipment SET name = ('{0}') WHERE idEquipment = ({1})"
                                .format(equipment.name, result[0]))
                    cur.execute("UPDATE equipment SET power = ({0}) WHERE idEquipment = ({1})"
                                .format(equipment.power, result[0]))
                else:
                    cur.execute("INSERT INTO equipment (name, power, User_cpf) VALUES ('{0}', {1}, '{2}')"
                                .format(equipment.name, equipment.power, app.current_user))
                db.commit()
            except MySQLdb.Error as err:
                db.rollback()
                QMessageBox.critical(app, 'Error!', 'Could not save changes on Equipments.\n\n{0}'.format(err))
            else:
                success = True

        if success:
            QMessageBox.information(app, 'Success!', 'Changes on Equipments successfully saved!')


class AgencyIO(object):

    @staticmethod
    def fetch_all(app):
        """Fetches all data from Agency table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM agency")
            agencies = cur.fetchall()

            for agency in agencies:
                e.append(Agency(agency[1], agency[2]))
                row_position = app.agency_table.rowCount()
                app.agency_table.insertRow(row_position)
                app.agency_table.setItem(row_position, 0, QtGui.QTableWidgetItem(agency[1]))
                app.agency_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency[2]))
                app.agency_table.setItem(row_position, 2, QtGui.QTableWidgetItem('-'))
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Equipment data from database')
        finally:
            cur.close()

    @staticmethod
    def save(agencies, app):
        """Saves all changes to database"""

        db = app.db
        cur = db.cursor()

        app.manager_input_agency.clear()
        success = False
        for agency in agencies:
            try:
                cur.execute("SELECT * FROM agency WHERE (address, city) = ('{0}', '{1}')"
                            .format(agency.address, agency.city))
                agency_id = cur.fetchone()
                if agency_id is not None:
                    cur.execute("UPDATE agency SET address = ('{0}') WHERE idAgency = ({1})"
                                .format(agency.address, agency_id[0]))
                    cur.execute("UPDATE agency SET city = ('{0}') WHERE idAgency = ({1})"
                                .format(agency.city, agency_id[0]))
                else:
                    cur.execute("INSERT INTO agency (address, city) VALUES ('{0}', '{1}')"
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
        """Fetches all data from Agency table"""

        db = app.db
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM agency")
            agencies = cur.fetchall()

            for agency in agencies:
                e.append(Agency(agency[1], agency[2]))
                row_position = app.agency_table.rowCount()
                app.agency_table.insertRow(row_position)
                app.agency_table.setItem(row_position, 0, QtGui.QTableWidgetItem(agency[1]))
                app.agency_table.setItem(row_position, 1, QtGui.QTableWidgetItem(agency[2]))
                app.agency_table.setItem(row_position, 2, QtGui.QTableWidgetItem('-'))
        except MySQLdb.Error:
            QMessageBox.critical(app, 'Error!', 'Unable to fetch Equipment data from database')
        finally:
            cur.close()

    @staticmethod
    def save(agencies, app):
        """Saves all changes to database"""

        db = app.db
        cur = db.cursor()

        success = False
        for agency in agencies:
            try:
                cur.execute("SELECT * FROM agency WHERE (address, city) = ('{0}', '{1}')"
                            .format(agency.address, app.city))
                result = cur.fetchone()
                if result is not None:
                    cur.execute("UPDATE agency SET address = ('{0}') WHERE idAgency = ({1})"
                                .format(agency.address, result[0]))
                    cur.execute("UPDATE agency SET city = ('{0}') WHERE idAgency = ({1})"
                                .format(agency.city, result[0]))
                else:
                    cur.execute("INSERT INTO agency (address, city) VALUES ('{0}', '{1}')"
                                .format(agency.address, agency.address))
                db.commit()
            except MySQLdb.Error as err:
                QMessageBox.critical(app, 'Error!', 'Could not save changes on Agencies.\n\n{0}'.format(err))
            else:
                success = True

        if success:
            QMessageBox.information(app, 'Success!', 'Changes on Agencies successfully saved!')


class SupportIO(object):

    @staticmethod
    def add(call, protocol):
        """Creates new object of Support"""

        support = Support(call, protocol)
        s.append(support)

    @staticmethod
    def update():
        """Lets user change some Support objects attributes"""

        protocol = raw_input('Support protocol:')
        flag = 0
        for support in s:
            if protocol == support.protocol:
                print 'Update support:'
                support.call = raw_input('Call:')
                support.protocol = raw_input('Protocol:')
                print 'Support updated!'
                flag = 1
        if flag == 0:
            print 'Support not found!'

    @staticmethod
    def delete():
        """Removes the Support object from data base"""

        protocol = raw_input('Support protocol:')
        flag = 0
        for support in s:
            if protocol == support.time:
                s.remove(protocol)
                flag = 1
                print 'Consumption removed from database!'
        if flag == 0:
            print 'Consumption not found!'

    @staticmethod
    def get():
        """Shows Consumption object attributes values"""

        protocol = raw_input('Consumption protocol:')
        flag = 0
        for support in s:
            if protocol == support.protocol:
                print support.__dict__
                flag = 1
        if flag == 0:
            print 'Support protocol not found!'

    @staticmethod
    def get_all():
        """Shows all registered Support object attributes values"""

        if s is not None:
            for support in s:
                print support.__dict__
        else:
            print "There ain't no Support registered yet"
