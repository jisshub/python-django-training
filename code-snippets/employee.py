import re

names = []
emp_file = open('employee.txt')
f_Contents = emp_file.read()
# employee = []
pattern = re.compile(r'\d{4,}')
salary = pattern.findall(f_Contents)
# print(salary)

new = f_Contents.split(',')
new2 = f_Contents.split('\n')
while '' in new2:
    new2.remove('')
print(new2)
sort_all = sorted(new2, key=lambda x: x[0], reverse=True)
print(sorted)

# for name in new2:
#     n = name[3:8]
#     names.append(n)
#
# print(names)
