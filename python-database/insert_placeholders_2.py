import mysql.connector

db = mysql.connector.connect(user='root',
                             password='passdb47',
                             host='localhost',
                             database='mydatabase')

cursor = db.cursor()

fname = input('Enter name:')
lname = input('Enter first name:')
age = int(input('Enter age:'))
gender = input('Enter sex: ')
sal = int(input('Enter name:'))

sql = """
 INSERT INTO employee VALUES(%s, %s, %s, %s, %s)"""

values = (fname, lname, age, gender, sal)


try:

    cursor.execute(sql, values)
    db.commit()

except Exception as err:
    print(err.args)

finally:
    db.close()
