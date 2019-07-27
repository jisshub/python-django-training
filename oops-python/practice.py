# Inheritance Exercise
# Multiple Inheritance


# Here class Makan inherits from multiple classes.
# when an instance is created,
# init method of Class Appachan is invoked automatically. bcause it is passed as first parameter
# in the class Makan. So the init method of class Ammachi is not invoked.


class Appachan:
    def __init__(self, hobby, hair_type):
        self.hobby = hobby
        self.hair = hair_type


class Ammachi:
    def __init__(self, hobby, blood_group):
        self.hobby = hobby
        self.group = blood_group


class Makan(Appachan, Ammachi):
    def unique(self, eyecolor):
        self.eyecolor = eyecolor
        return self.eyecolor


Appachan('dadad', 'dadad')


# to inherit the attributes of class Ammachi, v can define another method instead of init method,
# and call it explicitly.

# Second Example
class Appachan:
    def __init__(self, hobby, hair_type):
        self.hobby = hobby
        self.hair = hair_type


class Ammachi:
    def types(self, blood_group):
        self.group = blood_group


class Makan(Appachan, Ammachi):
    def unique(self, eyecolor):
        self.eyecolor = eyecolor
        return self.eyecolor


# third Example

# here class Ammachi is invoked since it is passed as first parameter in class Makan.
class Appachan:
    def __init__(self, hobby, hair_type):
        self.hobby = hobby
        self.hair = hair_type


class Ammachi:
    def __init__(self, blood_group):
        self.group = blood_group


class Makan(Ammachi, Appachan):
    def unique(self, eyecolor):
        self.eyecolor = eyecolor
        return self.eyecolor


# Another Examples
# here when isntance is created init methid is invoked, and the arguments.
class Appachan:
    def __init__(self, hobby, hair_type):
        self.hobby = hobby
        self.hair = hair_type


class Ammachi:
    def types(self, blood_group):
        self.group = blood_group


class Makan(Ammachi, Appachan):
    def unique(self, eyecolor):
        self.eyecolor = eyecolor
        return self.eyecolor


# Single Inheritance with method overriding

class Book:
    def __init__(self, material):
        self.material = material

    def details(self, pages, language):
        self.pages = pages
        self.lang = language

    def availabily(self):
        return 'Yes'


class Novel(Book):
    def details(self, pages, price):
        self.pages = pages
        self.price = price


# Multilevel Inheritance

class Bag:
    def __init__(self, material):
        self.mat = material

    def display(self):
        return f"My Bag material is {self.mat}"


class SchoolBag(Bag):
    def details(self, price, color):
        self.price = price
        self.color = color


class Handbag(SchoolBag):
    def details(self, price, color):
        self.price = price
        self.color = color
        return f"{self.price} and {self.color}"
