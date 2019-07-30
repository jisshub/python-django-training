# You can delete records from an existing table by using the "DELETE FROM" statement:
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='passdb47',
                               database='mydatabase')

cursor = mydb.cursor()
# to delete the record
cursor.execute('DELETE FROM customer WHERE id = 108')
print(f"{cursor.rowcount} records deleted")

# check whether record exists.
cursor.execute('SELECT * FROM customer')
print(cursor.fetchall())


