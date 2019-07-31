import mysql.connector

db_conn = mysql.connector.connect(user='root',
                                  host='localhost',
                                  password='passdb47',
                                  database='mydatabase')

cursor = db_conn.cursor()

# LIMIT THE NO OF RECORDS RETRIEVED USING LIMIT CLAUSE.
cursor.execute('SELECT * FROM customer WHERE name LIKE "%a%" ORDER BY id DESC LIMIT 2')

for cust in cursor:
    print(cust)





