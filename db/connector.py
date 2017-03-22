import MySQLdb


def get_db():

    db = MySQLdb.connect("localhost", "root", "root", "CEMIG")
    return db

