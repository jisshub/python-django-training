import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="passdb47"
)

print(mydb)