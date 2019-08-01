import mysql.connector

mydb = mysql.connector.connect(user='root',
                               host='localhost',
                               password='passdb47',
                               database='mydatabase')
cursor = mydb.cursor()

sql = """
        INSERT INTO employee VALUES(%s, %s, %s, %s);
        """

values = ('vijay', 'karan', 22, 'M', 40000)

try:
    cursor.execute(sql, values)
except:
    print('no data inserted')
finally:
    mydb.commit()

# here if exception raises in try block execpt block is xecuted.

