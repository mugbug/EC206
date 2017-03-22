import MySQLdb


class DataBaseConnector(object):

    @staticmethod
    def get_db():
        db = MySQLdb.connect("localhost", "root", "root", "CEMIG")
        return db

