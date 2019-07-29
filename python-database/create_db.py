import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='passdb47',
                               )
# use a method called cursor and create a cursor object

mycursor = mydb.cursor()

# use execute method of cursor object to write the query

mycursor.execute('CREATE DATABASE mydatabase')

# to check if database exist

mycursor.execute('SHOW DATABASES')

for i in mycursor:
    print(i)

# the result will be in separate tuples.


# connecting to the database newly created
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='passdb47',
                               database='mydatabase')

print(mydb)


