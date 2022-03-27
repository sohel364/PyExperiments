import mysql.connector
connection = mysql.connector.connect(host='localhost', user='root', password='admin')                            
mycursor = connection.cursor()
mycursor.execute("SHOW DATABASES")

for database in mycursor :
    print(database)



#Connection by json configuration
# config = {
#   'user': 'scott',
#   'password': 'password',
#   'host': '127.0.0.1',
#   'database': 'employees',
#   'raise_on_warnings': True
# }

# cnx = mysql.connector.connect(**config)