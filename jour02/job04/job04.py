import mysql.connector 

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="laplateforme"
)

mycursor = db.cursor()

mycursor.execute("SELECT nom, capacite FROM salles")

result = mycursor.fetchall()

for x in result:
    print(x)