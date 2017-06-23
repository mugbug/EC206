import MySQLdb
from PyQt4.QtGui import QMessageBox


class DataBaseConnector(object):

    @staticmethod
    def get_db(app):
        db_connection = False
        try:
            db = MySQLdb.connect(host='localhost', user='root', passwd='Petcovic10', db='mydb')
        except MySQLdb.Error as err:
            e = "Database connection error [%d]: %s" % (err.args[0], err.args[1])
        else:
            db_connection = True
        finally:
            if db_connection:
                print 'Database connection successful!'
                # QMessageBox.information(app, 'Notification', 'Database connection successful!')
                return db
            else:
                print e
                # QMessageBox.critical(app, 'Error!', 'Error trying to connect to database!\n{0}'.format(e))
                return 1

