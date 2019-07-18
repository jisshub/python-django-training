# Flow controls

# 1. Decision Making
# 2. iteration
# 3. Jumping


# age=int(input('Enter age: '))
# if age > 20:
#     print('u are eligible for voting')
# else:
#     print('not eligible')

# number = int(input('enter number: '))
# if number > 0:
#     print('positive')
# elif number < 0:
#     print('negative')
# else:
#     print('invalid')


# amount=int(input('Enter amount: '))
# max_amount=5000
# if amount>max_amount:
#     print('not enough money'
# elif amount<=max_amount:
#     print('withdraw')
# else:
#     print('ok')

# mark1 = int(input('Enter mark1: '))
# mark2 = int(input('Enter mark2: '))
# total = mark1 + mark2
# if total >= 90:
#     print('Grade A+')
# elif total >= 80 and total < 90:
#     print('Grade B')
# elif total >= 70 and total < 80:
#     print('Grade C')
# elif total >= 60 and total < 70:
#     print('Grade C+')
# else:
#     print('Passed')

# largest among 3 nos
# num1 = 34
# num2 = 23
# num3 = 11
# if num1 > num2:
#     if num1 > num3:
#         print(f"{num1} is greater than {num2} and {num3}")
#     else:
#         print(f"{num3} is greater than {num1} and {num2}")
# elif num2 > num3:
#     print(f"{num2} is greater than {num1} and {num3}")
# else:
#     print(f"{num3} if greater")


# iterations
# while , do-while, for
# age = int(input('Enter age: '))
# while age <= 18:
#     print('not satisfied for license')
#     # break
#     age = int(input('Enter age: '))
# print('satisfied for license')

# exercise
# import random
#
# i = 0
# random_int = random.randint(1, 10)
#
# while random_int != 5:
#     i += 1
#     random_int = random.randint(1, 10)
# print(i)


# using break in while
# x=0
# while x!=11:
#     print(x)
#     x+=2
#     if x==10:
#         break
#

# while with break keyword
# while True:
#     command = input('Whether light glows?: ')
#     if command == 'Yes'.lower():
#         break
#
# color = input('Enter Color: ')
# while color != 'purple':
#     color = input('Enter Color: ')


# reverse

# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# palindrome

# armstrong
# number = int(input('Enter a number: '))
# while number != 0:
#     digit = number % 10
#     result = digit ** 3
#     number //= 10
#
# if number is result:
#     print('armstrong')
# else:
#     print('not')

# For Loops

# for i in range(1,10):
#     if i%2==0:
#         print(i)

# for i in range(2,50,3):
#     print(i)


# Functions
#
# def hello_func():
#     pass
# hello_func()


# totaling values
# def total_marks(mark1, mark2):
#     res = mark1 + mark2
#     return res
#
#
# print(total_marks(34, 45))
# print(v)

# Collections

# parts = ['wheels', 'lights', 'headlamp', 'stereo']
# print(parts)
#
# parts.pop()

# list Methods
# drivers = ['Ram', 'Rahul', 'rajeev', 'amal']
# drivers.extend(['teena', 'varsha'])

# drivers.pop(2) - removing the value based on its index
# drivers.index('teena') - get the index of value

# sorting values in a list
# drivers.sort()
# print(drivers)

# data = ['bumrah', 'ajith', 'kumar', 'ceena']
# data.sort()
# print(data)
#
# # sort the value in reverse. default sort () sorts in alphabetical order
# data.sort(reverse=True)
#
# # default
# data.sort(reverse=False)
#
# colors = ['blue', 'green', ' violet']
# while 'red' not in colors:
#     color = input('Enter a color: ')
#     colors.append(color)
# print('ok')

# colors = ['blue', 'green', ' violet']
# for each in colors:
#     if each is 'red':
#         print('satisfied')
#     else:
#         color = input('Enter the color: ')
#         colors.insert(0, color)


# Balance details

# def bank()