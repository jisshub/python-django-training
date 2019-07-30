# When selecting records from a table, you can filter the selection by using the "WHERE" statement:
import mysql.connector

mydb = mysql.connector.connect(user='root',
                               host='localhost',
                               password='passdb47',
                               database='mydatabase')

cursor = mydb.cursor()
# cursor.execute('SELECT * FROM customer')
# print(cursor.fetchall())

# SELECTING ROW WITH ID 101

cursor = mydb.cursor()
cursor.execute("SELECT * FROM customer WHERE ID = 101 ")
print(cursor.fetchone())


# SELECTING COLUMNS WITH  A GIVEN ADDRESS
cursor.execute("SELECT name, id FROM customer WHERE address= 'Highway 34 '")
print(cursor.fetchall())

# USING LIKE OPERATOR WITH WHERE STATEMENT.

# WANT RECORDS OF CUSTOMER WHOSE NAME STARTS WITH LETTER 'J'.

# HERE V USE LIKE ALONG WITH A WILRDCARD '%'

cursor.execute('SELECT * FROM customer WHERE name LIKE "j%"')
print(cursor.fetchall())

cursor.execute('SELECT * FROM customer WHERE name LIKE "%Y"')
print(cursor.fetchall())


cursor.execute('SELECT * FROM customer WHERE address LIKE "%road%"')
print(cursor.fetchall())




