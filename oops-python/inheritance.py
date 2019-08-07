# here Cat class inherit the properties of Animal class.

class Animal:
    def __init__(self, name):
        self.name = name

    def details(self, species):
        self.species = species


class Cat(Animal):
    # pass
    def speak(self):
        return 'meow'


# an1 = Animal('dad')

class Hello:
    def run(self):
        for each in range(4):
            print('hello')


class Hi:
    def run(self):
        for each in range(4):
            print('hi')


t1 = Hello()
t2 = Hi()

t1.run()
t2.run()
class Parent:
    def phone(self):
        print('nokia')


class Child(Parent):
    pass


# Method Overriding
# here v override the bike method of parent class in child class.
# ie v create an instance of child class first, later v invoke
# bike method. so it prints the bike method in child class.
# incase if no bike method in child class later checks bike method in parent class and prints it..

class Parent:
    def phone(self):
        return 'Bluberry'

    def bike(self):
        # self.company = company
        return 'glamour'


class Child(Parent):
    def bike(self):
        # self.company = company
        return 'honda'


# Another  exampple
class Parent:
    def phone(self):
        return 'Bluberry'

    def bike(self):
        # self.company = company
        return 'glamour'


class Child(Parent):
    def bike(self, company):
        self.company = company

    def __str__(self):
        return self.company

# here v also print the company by doing
# print(instance name)
# when we print it , company is returned from str method

#

