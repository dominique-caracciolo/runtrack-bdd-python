import mysql.connector 

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="laplateforme"
)

mycursor = db.cursor()

mycursor.execute("SELECT sum(superficie) FROM etage")

result = mycursor.fetchone()

for x in result:
    print("La superficie total de la plateforme est de",x,"m2")