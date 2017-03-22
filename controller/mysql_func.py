import connector

class Insert():

    @staticmethod
    def insert_client(client):

        db = connector.get_db()
        cursor = db.cursor()

        sql = "INSERT INTO Client(Nome, \
                Endereco, CPF, Idade) \
                VALUES ('%s', '%s', '%s', '%d')"% \
                (client.name, client.address, client.cpf, client.age)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()




