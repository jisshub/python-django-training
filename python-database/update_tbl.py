import mysql.connector

db = mysql.connector.connect(user='root',
                             password='passdb47',
                             host='localhost',
                             database='mydatabase')

c = db.cursor()
c.execute('UPDATE customer SET name = "Styris" WHERE id = 102')
# use commit() else changes not saved.
db.commit()
# print(c.fetchall())

c.execute('SELECT * FROM customer')
print(c.fetchall())

