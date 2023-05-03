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
   print(x)

class Salarie:
   

