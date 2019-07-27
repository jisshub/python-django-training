# class Employee:
#     def __init__(self, id, name, sal, designation):
#         self.id = id
#         self.name = name
#         self.sal = sal
#         self.design = designation
#
#     def __str__(self):
#         return self.name
#

emp_file = open('sample_dir/employee.txt')
data1 = []
for each in emp_file:
    data1.append(each[:-1].split(','))
# print(data1)
data2 = sorted(data1, key=lambda y: y[2], reverse=True)
print(data2)
for sal in data2:
    if int(sal[2]) >= 19000:
        print(sal[1])
