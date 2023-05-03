import mysql.connector 

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  #database="DBemployes"
)

# print(db)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS DBemployes")
mycursor.execute("use DBemployes")
mycursor.execute("CREATE TABLE IF NOT EXISTS employes (id INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(255),prenom VARCHAR(255),salaire FLOAT ,id_service INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS services (id INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(255))")

mycursor.execute("INSERT IGNORE INTO services (nom) VALUES ('Pole Emploie')")
db.commit()

mycursor.execute("INSERT IGNORE INTO services (nom) VALUES ('Securite')")
db.commit()

mycursor.execute("INSERT IGNORE INTO services (nom) VALUES ('Chomage')")
db.commit()

emp_req = "INSERT IGNORE INTO employes (prenom, nom, salaire, id_service) VALUES (%s, %s, %s, %s)"
valeur = [
    ('Jeanmichmich','Dupres',2500.23, 1),
    ('Gaston','Baton',3444, 2),
    ('Michel','Dupont',4323.25, 3),
    ('Justine','Bridou',1260.31, 4),
    ('Justin','Bridure',6400.88, 5),
    ('Paul','Emploi',1666.55, 6)]

mycursor.executemany(emp_req, valeur)
db.commit()

salaire = "SELECT prenom, nom, salaire FROM employes WHERE salaire > 3000"
mycursor.execute(salaire)
result = mycursor.fetchall()


for x in result:
   print("Salaire a plus de 3000 euros:", x)

class Employee:
    columns = ['id', 'nom', 'prenom', 'salaire', 'id_service']

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def create_employee_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                prenom VARCHAR(255),
                salaire FLOAT,
                id_service INT
            )
        """)
        self.db.commit()

    def insert_employee(self, nom, prenom, salaire, id_service):
        self.cursor.execute("""
            INSERT INTO employes (nom, prenom, salaire, id_service)
            VALUES (%s, %s, %s, %s)
        """, (nom, prenom, salaire, id_service))
        self.db.commit()

    def get_employee_by_salary(self, seuil_salaire):
        self.cursor.execute("""
            SELECT * FROM employes WHERE salaire > %s
        """, (seuil_salaire,))
        result = self.cursor.fetchall()
        return result

    def update_employee_salary(self, id_employee, new_salaire):
        self.cursor.execute("""
            UPDATE employes SET salaire = %s WHERE id = %s
        """, (new_salaire, id_employee))
        self.db.commit()

    def delete_employee(self, id_employee):
        self.cursor.execute("""
            DELETE FROM employes WHERE id = %s
        """, (id_employee,))
        self.db.commit()

    def __del__(self):
        self.db.close()


