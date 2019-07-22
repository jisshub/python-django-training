# square of numbers using list comprehension

squares = [each ** 2 for each in range(1, 7)]
print(squares)

# cartseian product of two list
a = [2, 3, 4]
b = [1, 5, 8]
cart = [(i, j) for i in a for j in b]
print(cart)

# employee uing list comprehension
employee = [('ajith', 4000), ('aju', 300000), ('kumar', 21000)]
data = [each[0] for each in employee if each[1] > 18000]
print(data)
# count the employees
print(len(data))

# employee names starting with string 's'

employee = ['sachin', 'sehwag', 'ajith']
new = [each for each in employee if each[0] == 's']
print(new)

# one away edit









