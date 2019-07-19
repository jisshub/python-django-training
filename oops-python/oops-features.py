# polymorphism

# method overloading
# same method bt different no. of arguments

class Laptop:
    def details(self, model):
        self.model = model

    def details(self, price, os):
        self.price = price
        self.os = os


lap1 = Laptop()


# here only the second method can only be invoked.
# ie both cant be invoked.

class Clothes:
    brand_name = 'Levis'

    def __init__(self, material):
        self.material = material

    def features(self, type, color):
        self.type = type
        self.color = color

    def features(self, size, wash):
        self.size = size
        self.wash = wash




