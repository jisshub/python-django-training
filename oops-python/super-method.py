# super() refer to the parent class or base class

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()


# we called __init__ method of the Mammal class using super().


# Example -2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)


# Here, you’ve used super() to call the __init__() of the Rectangle class, allowing you to use it in the Square class
# without repeating code.


# super() in multiple inheritance

# Example -3

# by using super class, v refer to the parent class A.
# and code inside it will be executed first.

class A:
    def __init__(self):
        print('first')


class B:
    def __init__(self):
        print('second')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('third')


#
# C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# Practice
import math


class Cylinder:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


class Cone(Cylinder):
    def __init__(self, radius, height):
        super().__init__(radius, height)


class Triangle(Cylinder):
    def __init__(self, radius, height):
        super().__init__(radius, height)

    def Area(self, width):
        self.width = width
        return .5 * self.width * self.height


class Sqn(Cone, Triangle):
    def __init__(self, radius, height):
        super().__init__(radius, height)


# practice
class Squre:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display(self):
        return self.length + self.width


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print(self.length * self.width)

    def displaynew(self):
        return self.length * self.width


class Area(Squre, Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
