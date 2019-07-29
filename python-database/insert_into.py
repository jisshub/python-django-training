import mysql.connector

mydb = mysql.connector.connect(user='root',
                               password='passdb47',
                               database='mydatabase',
                               host='localhost')

cursor = mydb.cursor()
# INSERTING A SINGLE ROW
query = 'INSERT INTO customer VALUES(%s, %s, %s)'
# then pass the values to each %s in the form of a tuple.
values = ('John', 101, 'HIghway 21')
# tHEN EXECUTE THE CURSOR
cursor.execute(query, values)

# mydb.commit(). It is required to make the changes, otherwise no changes are made to the table. ie if not
# used returns an empty set.
mydb.commit()

print(cursor.rowcount, 'records inserted')
# rowcount gives the count of rows inserted to the table.


# NOTE:
# In SQL, the %s signals parameter insertion. This sends your query and data to the server separately.


# INSERING MULTIPLE ROWS TO THE TABLE

query = 'INSERT INTO customer VALUES(%s)'





