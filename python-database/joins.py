import mysql.connector

db_conn = mysql.connector.connect(user='root',
                                  host='localhost',
                                  password='passdb47',
                                  database='mydatabase')

my_cursor = db_conn.cursor()

# INNER JOIN
sql = """
    SELECT department, country FROM employees INNER JOIN regions ON employees.region_id = regions.region_id;
        """

my_cursor.execute(sql)
for i in my_cursor:
    print(i)
