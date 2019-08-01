# operator overloading examples:

class Tank:
    def __init__(self, quanity):
        self.quantity = quanity

    def __add__(self, other):
        return self.quantity + other.quantity


c1 = Tank(30)
c2 = Tank(40)
print(c1 + c2)


class Tank:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f"{self.quantity},{other.quantity}"


c1 = Tank(30)
c2 = Tank(40)
print(c1 + c2)


# here v returs 30 and 40
# note here other keyword receives the argument 40 of object c2.


class Tank:
    def __init__(self, quantity):
        self.quant = quantity

    def __mul__(self, other):
        return self.quant * other.quant


t1 = Tank(40)
t2 = Tank(30)

print(t1 * t2)


# more than 2 objects

class Tank:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        self.quantity += other.quantity
        tk = Tank(self.quantity)
        return tk

    def __str__(self):
        return str(self.quantity)


t1 = Tank(40)
t2 = Tank(30)
t3 = Tank(50)

add = t1 + t2 + t3
print(add)

# here v add 3 objects together, initially we add the t1 and t2 which gives 70 and when v add it
# with an object type t3 it throws error. since we r tyring to add an objrct type with an int type.

