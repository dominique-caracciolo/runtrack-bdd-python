import mysql.connector 

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="laplateforme"
)

# print(db)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE etage (id INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(255),numero INT, superficie INT)")
mycursor.execute("CREATE TABLE salles (id INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(255),id_etage INT, capacite INT)")
mycursor.execute("show TABLES")

result = mycursor.fetchall()

for x in result:
    print(x)