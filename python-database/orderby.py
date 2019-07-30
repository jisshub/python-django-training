# Use the ORDER BY statement to sort the result in ascending or descending order.
#
# The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order,.exe
# use the DESC keyword.


import mysql.connector

mydb = mysql.connector.connect(user='root',
                               password='passdb47',
                               host='localhost',
                               database='mydatabase')

cursor = mydb.cursor()

cursor.execute('SELECT * FROM customer ORDER BY name')
print(cursor.fetchall())


cursor.execute('SELECT * FROM customer ORDER BY name DESC')
print(cursor.fetchall())



