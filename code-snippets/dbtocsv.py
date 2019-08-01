from csv import writer, reader
import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='passdb47',
                               database='mydatabase')
cur_obj = mydb.cursor()
sql = """
        SELECT first_name, departments.department, division, salary FROM employees INNER JOIN  
         departments ON employees.department = departments.department ORDER BY first_name LIMIT 10; 
        """
cur_obj.execute(sql)

with open('employees.csv', 'w') as file:
    writer_obj = writer(file)
    writer_obj.writerow(['name', 'departments', 'division', 'salary'])
    for each in cur_obj:
        writer_obj.writerow([each[0], each[1], each[2], each[3]])

with open('employees.csv', 'r') as file_2:
    reader_obj = reader(file_2)
    # to skip the header of the files and move to next row.
    next(reader_obj)
    for each in reader_obj:
        print(each)


