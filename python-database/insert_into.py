import mysql.connector

mydb = mysql.connector.connect(user='root',
                               password='passdb47',
                               database='mydatabase',
                               host='localhost')

cursor = mydb.cursor()
# INSERTING A SINGLE ROW
query = 'INSERT INTO customer VALUES(%s, %s, %s)'
# then pass the values to each placeholder %s in the form of a tuple.
values = ('John', 101, 'HIghway 21')
# tHEN EXECUTE THE CURSOR
cursor.execute(query, values)

# mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
mydb.commit()

print(cursor.rowcount, 'records inserted')
# rowcount gives the count of rows inserted to the table.


# NOTE:
# In SQL, the %s indicates a placeholder.


# INSERING MULTIPLE ROWS TO THE TABLE
# to insert multiple rows to the table, use executemany() method instead of execute()

query = 'INSERT INTO customer VALUES (%s, %s, %s)'

# values given in tuples wich are enclosed in a list and passed to the exeutemany() method.
values = [('Jacob', 102, 'Hignhway 32'),
          ('Dhruv', 103, 'Highway 34'),
          ('Sandy', 104, 'Ocean blvd 2'),
          ('Betty', 105, 'Green Grass 1')]
#
# cursor.executemany(query, values)
mydb.commit()
print(cursor.rowcount, 'records inserted')

# Example:
values = [('Andy', 108, 'Main Road 989'),
          ('Muaary', 109, 'Baker street 55')]
cursor.executemany(query, values)
mydb.commit()
print(f"{cursor.rowcount} records inserted")



