import sys


def square():
    print(4 ** 2)
    square()


square()


# factorial of a number using Recurion

def factorial(num):
    # while
    if num == 1:
        return num
    print(num * factorial(num - 1))


print(factorial(3))


