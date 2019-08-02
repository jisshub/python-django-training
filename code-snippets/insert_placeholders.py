import mysql.connector

db = mysql.connector.connect(user='root',
                             password='passdb47',
                             host='localhost',
                             database='mydatabase')

cursor = db.cursor()
try:
    sql = """
    INSERT INTO employee VALUES(%s, %s, %s, %s, %s)' 
        
        
    """
    values = ('Arun', 'Kumar', 23, 'M', 10000)
    cursor.execute(sql, values)
    db.commit()
except Exception as e:
    print(e.args)

finally:
    db.close()
