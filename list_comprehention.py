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

# find all numbers that r divible by 7

mod7 = [each for each in range(1, 1000) if each % 7 is 0]
print(mod7)

# fin all numbers that have 3 in them

return3 = [num for num in range(1, 100) if '3' in str(num)]
print(return3)

# example4
nums = list('385638')
d = [each for each in nums]
print(d)

# remove all vowels in a string
consonants = [each for each in 'jissmon'.upper() if each not in 'AEIOU']
print(consonants)

# to create a (letter, number) pair
number = list('56789')
letter = ['A', 'B', 'C', 'D', 'E']
new = [(each, each2) for each in number for each2 in letter]
print(new)

# return the intersection of two list
num1 = [1, 2, 3, 4]
num2 = [3, 4, 5, 6]
new = [n for n in num1 for n2 in num2 if n is n2]
print(new)


# reverse and change case

def new(names):
    new = [name[::-1].lower() for name in names]
    return new


print(new(['Jiss', 'Jose', 'Ajith']))
