# using init method and class method

# class Cars:
#     def __init__(self):
#         print('hai')
#
#
# car1 = Cars()
#
#
# class Cars:
#     def display(self):
#         print('hi')
#
#
# car2 = Cars()

# here in init method is called automaticaly while the instance is created
# incase of class mthod display, v need to explicitly invoke that method to print the result


# here automatically invode the init method while an instance is created.

class Cars:
    company_name = 'Hyundai'

    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    def display(self):
        return f"{self.model} and {self.mileage}"

    def __str__(self):
        return self.model
        # return self.mileage

# here __str__() is invoked automatically while an instance is created.



