import mysql.connector

db = mysql.connector.connect(user='root',
                             password='passdb47',
                             host='localhost',
                             database='mydatabase')

cursor = db.cursor()

cursor.execute('DELETE FROM employee WHERE first_name LIKE "s%"')

db.commit()

