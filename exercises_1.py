# Least positive Integer

numbers = []

# print(numbers)
while len(numbers) < 5:
    num = int(input('numbers: '))
    numbers.append(num)
# print(numbers)
for each in numbers:
    if each > 0:
        if each == min(numbers):
            print(each)
    else:
        print('negative')


# numbers=[]
# def least_positive(numbers):
#     global numbers
#     while len(numbers) < range()


# sqaure of n numbers.

def find_square(number):
    for each in range(1, number):
        print(each ** 2)


number = int(input('Enter limit'))
find_square(number)

# square of numbers using list comprehension

squares = [each ** 2 for each in range(1, 7)]
print(squares)
# square of n numbers using a function
empty = []


def find_square(number):
    global empty
    for each in range(1, number):
        sq = each ** 2
        empty.append(sq)
    return empty


number = int(input('Enter limit'))
ret = find_square(number)
print(ret)

remainders = []


def remainder(limit):
    global remainders
    for each in range(limit):
        rem = each % 2
        remainders.append(rem)
    return remainders


limit = int(input('Enter Limit: '))
print(remainder(limit))

# convert to uppercase

names_upper = []


def upper_conv(names):
    for each in names:
        names_upper.append(each.upper())
    return names_upper


names = ['jissmon', 'jose', 'ajith']
print(upper_conv(names))


# names_upper = []


def upper_conv(names):
    for each in names:
        names.append(each.upper())
    return names


names = ['jissmon', 'jose', 'ajith']
print(upper_conv(names))
