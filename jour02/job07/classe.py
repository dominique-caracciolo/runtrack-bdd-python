import mysql.connector
class Employe:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin",
            database="DBemployes"
        )
        self.cursor = self.mydb.cursor()

    def create_employes(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.mydb.commit()
        return self.cursor.lastrowid

    def read_employes(self):
        query = "SELECT * FROM employes"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def read_by_id_employes(self, id):
        query = "SELECT * FROM employes WHERE id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def update(self, id, nom, prenom, salaire, id_service):
        query = "UPDATE employes SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s"
        values = (nom, prenom, salaire, id_service, id)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_employes(self, id):
        query = "DELETE FROM employes WHERE id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        self.mydb.commit()

db= Employe()
