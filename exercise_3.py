# Employee with highest salary
employee = [('ajith', 4000), ('aju', 300000)]
# print(employee[1][1])
for each in employee:
    if each[1] > 18000:
        print(each[0])

emp = []


def high_sal(employee):
    for each in employee:
        if each[1] > 18000:
            # print(each[0])
            emp.append(each[0])
    print(emp)


high_sal([('ajith', 4000), ('aju', 300000), ('kumar', 21000)])

# using list comprehensios

employee = [('ajith', 4000), ('aju', 300000), ('kumar', 21000)]
data = [each[0] for each in employee if each[1] > 18000]
print(data)

# most frequently yoccuring words in a sentence
#
# sentence = 'hai how hai where each hai'
#
# count = 0
#
#
# def ferquent(sentence):
#     global count
#     new_se = sentence.split()
#     for each in new_se:
#         if each:
#             count += 1
