import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='passdb47',
                               database='mydatabase')

cursor = mydb.cursor()

cursor.execute('CREATE TABLE customer(NAME VARCHAR(20), ID INT NOT NULL PRIMARY KEY, '
               'address VARCHAR(30))')

# check whether table exists.
cursor.execute('SHOW TABLES')
for tbl in cursor:
    print(tbl)


