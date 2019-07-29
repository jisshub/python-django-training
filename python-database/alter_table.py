import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='passdb47',
                               database='mydatabase')

# alter table customer by maKing ID column autoincrement

my_cursor = mydb.cursor()
# # CHECK TABLE EXIST IF SO, IT SHOWS ERROR
my_cursor.execute('CREATE TABLE customer(NAME VARCHAR(20), ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                  'ADDRESS VARCHAR(30))')

# SO ALTER IT USING MODIFY
# when v alter the table dont use primary key for id again since once it is already set as a primary key.

my_cursor.execute('ALTER TABLE customer MODIFY COLUMN ID INT NOT NULL AUTO_INCREMENT')

# view the change by using describe statement.
my_cursor.execute('DESC customer')
for i in my_cursor:
    print(i)


# ALTER BY ADD, DROP
import mysql.connector

mydb = mysql.connector.connect(user='root',
                               host='localhost',
                               password='passdb47',
                               database='mydatabase')
my_cursor = mydb.cursor()

# ALTER TABLE BY ADDING A NEW COLUMN CALLED AGE
my_cursor.execute('ALTER TABLE customer ADD COLUMN age INT')

# ALTER TABLE BY DROPPING A COLUMN
my_cursor.execute('ALTER TABLE customer DROP COLUMN age')

# show columns from table.
my_cursor.execute('SHOW COLUMNS FROM customer')
for each in my_cursor:
    print(each)
