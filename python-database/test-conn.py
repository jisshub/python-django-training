# connecting mysql with python
import mysql.connector

# pass connection required keyword arguments to the connect method
db_conn = mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='passdb47',
                                  database='shop')
print(db_conn)



