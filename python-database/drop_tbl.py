# You can delete an existing table by using the "DROP TABLE" statement:

import mysql.connector

mydb = mysql.connector.connect(user='root',
                               password='passdb47',
                               host='localhost',
                               database='mydatabase')

cursor = mydb.cursor()
cursor.execute('DROP TABLE customer')

# check whether it exists
cursor.execute('desc customer')




