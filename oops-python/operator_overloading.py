# OPERATOR OVERLOADING


class Books:

    def __init__(self, pages):
        self.pages = pages


b1 = Books(300)
b2 = Books(400)
print(b1 + b2)


# here v cant add both the objects since it is an object type

# here can use special method or magic method called add()
# ie. __add__()


class Books:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        # return 'hello'

        return self.pages + other.pages


b1 = Books(300)
b2 = Books(400)
print(b1 + b2)


# here while v perfrom '+' operation of two objects,
# then special method called add is invoked.
# here self points to object b1 and other keyword points to other objects.

# similarly there are special methods for each operators

class Books:

    def __init__(self, pages):
        self.pages = pages

    def __sub__(self, other):
        # return 'hello'

        return other.pages - self.pages


b1 = Books(300)
b2 = Books(400)
print(b1 - b2)


# adding 3 objects at  a time
class Books:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        bk = Books(self.pages + other.pages)
        return bk

    def __str__(self):
        return str(self.pages)


b1 = Books(300)
b2 = Books(400)
b3 = Books(100)
add = b1 + b2 + b3
print(add)
print(type(add))


# here v initially perform b1 + b2 and later add it with b3
# it returns error since b1+b2 is an int type and v add it with an object type b3
# so we add first two objects and later add it  with third object and finally convert it to an object type
# Thus v can add all three together.


