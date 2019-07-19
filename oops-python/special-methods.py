# using init method

class Cars:
    def __init__(self):
        print('hai')


car1 = Cars()


# without init method
class Cars:
    def display(self):
        print('hi')


car2 = Cars()


# here init method is called automaticaly while the instance is created
# incase of class method display, v need to explicitly invoke that method to print the result
# here v automatically invoke the init method while an instance is created.


# another example of init method
class Animal:

    def __init__(self, species, weight):
        self.species = species
        self.weight = weight


animal = Animal('Siberian Tiger', 400)


# here by using init method v can pass the arguments to the parameters
# in the init method when the instance is created.

# if not, we need to explicitly invoke a method after creating an instance
# and then need to pass the required arguments to the parameters specified.


class Cars:

    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    def display(self):
        return f"{self.model} and {self.mileage}"

    def __str__(self):
        return self.model
        # return self.mileage


# here __str__() is invoked automatically while an instance is created.

# using this method we can return a string that represent the object instead of getting memory
# address of that object.
# so here v return model which isa string type, so when v do
#         print(objectname)
# it returns the model which specified in the str method.
# here model is only returned since it is a string type.
# which means shows error when try to return any non string type.


# Another Example for str method

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        # return self.name
        return self.height


per1 = Person('sjl', 5.6, 11)

# it shows error when we do
#         print(per1)
# since v return a height which is an integer type.
