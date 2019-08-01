class Employee:
    def __init__(self, id, name, sal, designation):
        self.id = id
        self.name = name
        self.sal = sal
        self.design = designation

    def __str__(self):
        return self.name

emp_file = open('employee.txt')
# data1 = []
emp_list = []
for each in emp_file:
    data1 = (each[:-1].split(","))
    print(data1)
    emp_list.append(Employee(data1[0], data1[1], data1[2], data1[3]))
print(emp_list)
sorted_names = sorted(emp_list, key=lambda emp: emp.name, reverse=False)
for val in sorted_names:
    print(val)
data2 = sorted(emp_list, key=lambda emp: emp.name, reverse=True)
for sal in data2:
    print(sal)
