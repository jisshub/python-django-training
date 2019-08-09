class Birds:
    def __init__(self):
        self.feathers = True
        self.wings = True
        self.four_legs = False


class Flying(Birds):
    def fly(self):
        return "they can fly"

    def speak(self):
        return 'can speak'


class Nonflying(Birds, Flying):
    def fly(self):
        return 'cant fly'


obj = Nonflying()

# it throws an error
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Birds, Flying.
# since flying already inherits from birds class python cant determine from which class the method shud be called.

# floow the link below to resolve the issue.


'https://stackoverflow.com/questions/29214888/typeerror-cannot-create-a-consistent-method-resolution-order-mro'


class Birds:
    def __init__(self):
        self.feathers = True
        self.wings = True
        self.four_legs = False


class Flying(Birds):
    def fly(self):
        return "they can fly"

    def speak(self):
        return 'can speak'


class Nonflying(Flying):
    def fly(self):
        return 'cant fly'


obj = Nonflying()
obj.speak()
