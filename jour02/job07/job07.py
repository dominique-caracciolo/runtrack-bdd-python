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

from classe import Employe

db = Employe()
id = db.create_employes("Dupont", "Jean", 2500.23, 1)
print("Le nouvel employé a été créé avec l'ID:", id)
employe = db.read_by_id_employes(id)
print("L'employé avec l'ID", id, "est:", employe)
db.update(id, "Dupont", "Jean-Michel", 3000, 1)
print("L'employe avec l'id",id," a etais mis a jour")
db.delete_employes(id)
print("L'employer avec l'id",id,"a etais supprimer")
