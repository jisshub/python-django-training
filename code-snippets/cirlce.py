import math


class Circle:
    # pi = 3.14

    def __init__(self, radius):
        self.rad = radius
        self.pi = math.pi

    def area_circle(self):
        area = self.pi * self.rad ** 2
        return area

    def peri_circle(self):
        perimeter = 2 * self.pi * self.rad
        return perimeter


obj1 = Circle(5)
obj1.peri_circle()
obj1.area_circle()
