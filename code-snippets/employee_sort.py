# import re
#
# list1 = []
#
#
# def employee_sort():
#     with open('sample_dir/employee.txt') as emp_file:
#         # here v store each line of file to a list.
#         f_cont = emp_file.readlines()
#     # remove \n from all elements in the list
#     f_cont = list(map(lambda f: f.strip(), f_cont))
#     sort_it = (sorted(f_cont, key=lambda x: x[2], reverse=False))
#     # create a pattern to match al   l non digits characters.
#     pattern = re.compile(r'\D+')
#     for each in sort_it:
#         match = re.findall(pattern, each)[0]
#         list1.append(match)
#     f_cont = list(map(lambda f: f.strip(','), list1))
#     return f_cont
#
#
# emp = employee_sort()
# print(emp)


# using classes
import re

list1 = []


class Employee:
    def __init__(self):
        pass

    def employee(self):
        global list1
        with open('sample_dir/employee.txt') as emp_file:
            f_cont = emp_file.readlines()
            f_cont = list(map(lambda x: x.strip(), f_cont))
            sort_it = sorted(f_cont, key=lambda k: k[1], reverse=False)
            pattern = re.compile(r'\D+')
            for each in sort_it:
                match = re.findall(pattern, each)[0]
                list1.append(match)
            f_cont = list(map(lambda f: f.strip(','), list1))
            return f_cont


a = Employee()
print(a.employee())
# a.employee()


