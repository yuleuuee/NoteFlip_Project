#this code is only for creating a databse , that is "Notefilp_users" in MySQL

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    passwd = "rabhav9861",
    auth_plugin='mysql_native_password'
)

my_cursor = mydb.cursor()

# just creating a database name "Notefilp_users" 
# my_cursor.execute("CREATE DATABASE IF NOT EXISTS Notefilp_users") 
                  
my_cursor.execute("SHOW DATABASES") 
for db in my_cursor:
    print(db)