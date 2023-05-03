import mysql.connector 

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="laplateforme"
)

cursor = db.cursor()
#print(db)

etage_req = "INSERT INTO etage (nom, numero, superficie) VALUES (%s, %s, %s)"
valeur_etage = [('RDC',0,'500'), 
                ('R+1',1,'500')]
                
salles_req = "INSERT INTO salles (nom, id_etage, capacite) VALUES (%s, %s, %s)"
valeur = [('Lounge',1,'100'),
('Studio Son',1,'5'),
('Broadcasting',2,'50'),
('Bocal Peda',2,'4'),
('Coworking',2,'80'),
('Studio Video',2,'5')]
cursor.executemany(etage_req, valeur_etage)
cursor.executemany(salles_req, valeur)
db.commit()

# result = cursor.fetchall()
# for x in result:
#     print(x)

db.close()