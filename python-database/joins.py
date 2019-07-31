import mysql.connector

db_conn = mysql.connector.connect(user='root',
                                  host='localhost',
                                  password='passdb47',
                                  database='mydatabase')

my_cursor = db_conn.cursor()

# BASIC JOIN
sql = """
        SELECT first_name, last_name, division, departments.department FROM employees, departments 
        WHERE employees.department = departments.department;
"""
my_cursor.execute(sql)
for details in my_cursor:
    print(details)

# # INNER JOIN
sql = """
    SELECT department, country FROM employees INNER JOIN regions ON employees.region_id = regions.region_id;
        """

my_cursor.execute(sql)
for i in my_cursor:
    print(i)

# LEFT JOIN
#
sql = """
        SELECT DISTINCT employees.department, departments.department FROM employees LEFT JOIN departments ON
        employees.department = departments.department
        """

my_cursor.execute(sql)
for dept in my_cursor:
    print(dept)

# RIGHT JOIN

sql = """
        SELECT DISTINCT employees.department, departments.department FROM employees RIGHT JOIN departments ON 
        employees.department = departments.department 
        """

my_cursor.execute(sql)
for dept in my_cursor:
    print(dept)
