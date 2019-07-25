# emp_data = {'ajith': 3000, 'kumar': 2000, 'jiss': 1000}

emp = []


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.sal = salary

    def __str__(self):
        # emp.append((self.name, self.sal))

        return self.name


def getEname(emplo):
    return emplo.name


emp1 = Employee('jiss', 2000)
emp2 = Employee('ajith', 4000)
emp = [emp1, emp2]
# name_sorted = sorted(emp, key=getEname)
name_sorted = sorted(emp, key=lambda n: n.name)
for e in name_sorted:
    print(e)
# print(name_sorted)


# Sorting Based on salaries
emp = []


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.sal = salary

    def __str__(self):
        # emp.append((self.name, self.sal))

        return self.name
        # pass


emp1 = Employee('jiss', 2000)
emp2 = Employee('ajith', 4000)
emp3 = Employee('aad', 1000)
emp = [emp1, emp2, emp3]
print(emp)

name_sorted = sorted(emp, key=lambda s: s.sal)
for e in name_sorted:
    print(e)
# print(name_sorted)




