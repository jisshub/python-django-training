def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b

#
# if __name__ == '__main__':
#     print(add(10, 20))
#     print(multiply(10, 20))
#     print(division(10, 20))
