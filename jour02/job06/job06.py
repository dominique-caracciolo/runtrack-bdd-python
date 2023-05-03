import mysql.connector 

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="laplateforme"
)

mycursor = db.cursor()

mycursor.execute("SELECT sum(capacite) FROM salles")

result = mycursor.fetchone()

for x in result:
    print("La capacite de toutes les salles est de :",x)