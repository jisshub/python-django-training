# fetch data from db

import mysql.connector

mydb = mysql.connector.connect(user='root',
                               password='passdb47',
                               host='localhost',
                               database='mydatabase')

cursor = mydb.cursor()
# try:
#
#     cursor.execute('SELECT * FROM employee;')
#     result = cursor.fetchall()
#     for each in result:
#         print(each)
# except Exception as err:
#     print(err.args)
# finally:
#     mydb.close()


# here try block raises an exception thus except block is execuuted.

# try:
#
#     cursor.execute('SELECT * FROM emplosdfbsfjyee;')
#     result = cursor.fetchall()
#     for each in result:
#         print(each)
# except Exception as err:
#     print(err.args)
# finally:
#     mydb.close()


# try:
#     sql = """
#         SELECT * FROM employee WHERE income > 30000;
#     """
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for emp in result:
#         print(emp)
#
# except Exception as err:
#     print(err.args)
#
# finally:
#     mydb.close()
#


# using like operator in sql

try:

    sql = """
    
            SELECT * FROM employee WHERE first_name LIKE 's%' 
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    for emp in result:
        print(emp)
except Exception as err:
    print(err.args)

finally:
    mydb.close()


