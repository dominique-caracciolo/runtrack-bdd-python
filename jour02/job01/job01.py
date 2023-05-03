import mysql.connector 

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="laplateforme"
)

print(db.database)
mycursor = db.cursor()
# mycursor.execute("use laplateforme")
mycursor.execute("SELECT * FROM etudiants")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)