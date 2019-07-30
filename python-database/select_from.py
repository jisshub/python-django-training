import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='passdb47',
                               database='mydatabase')
#
cursor = mydb.cursor()
# # selecting all rows from a table, use fetchall() method to get all rows.
cursor.execute('SELECT * FROM customer')
myresult = cursor.fetchall()
# fetchall() returns a list of tuples each composed of row values.
# can loop thru it.
for cust in myresult:
    print(cust)

# # selecting first row from the table. use fetchone() method of cursor object
cursor = mydb.cursor()
new = cursor.execute('SELECT * FROM customer')
print(cursor.fetchone())

# # SELECTING A COLUMN FROM A TABLE
cursor = mydb.cursor()
cursor.execute('SELECT address FROM customer')
result = cursor.fetchall()
for i in result:
    print(i)


# SELECTING FIRST COLUMN VALUE OF NAME FIELD
cursor = mydb.cursor()
cursor.execute('SELECT name FROM customer')
first_val = cursor.fetchone()
print(first_val)
