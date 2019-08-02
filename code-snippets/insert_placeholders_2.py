import mysql.connector

db = mysql.connector.connect(user='root',
                             password='passdb47',
                             host='localhost',
                             database='mydatabase')

cursor = db.cursor()

# age = int(input('Enter name:'))
# fname = input('Enter first name:')
# lname = input('Enter name:')
# gender = input('Enter sex: ')
# sal = int(input('Enter name:'))

sql = """
 INSERT INTO employee VALUES(%s, %s, %d, %s, %d)""" % \
      ('ajith', 'kumar', 45, 'F', 40000)

try:

    cursor.execute(sql)
    db.commit()

except Exception as err:
    print(err.args)

finally:
    db.close()
