# class methods
# to change  only the class variables. bt cant modify any instance attributes.
# for class methods v use cls as parameter instead of using self(used in instance and special methods.)
# and when class method is invoked , cls points to class instead of pointing to the instance


# when v try to invoke a class method using the classname it throws err if decorator not used before the method.
# decorator for class method is '@classmethod'


class Student:
    institute = 'Luminar'

    def __init__(self, course):
        self.course = course

    @classmethod
    def info(cls):
        cls.institute = 'Steps'

        return cls.institute

    def change_course(self):
        self.course = 'Java'
        return self.course


stud1 = Student('Python')


#
# class Employee:
#     company_name = 'TCS'
#     def __init__(self,name):
#         self.name=name
#     def salary(self):
#


# Static Method

# its not a class method, instance method, and cant use any instance variable.
# dont take any self or cls parameters
# cant modify instance attributes, class variables.

# if v dont use decorator for static method it throws error while try to invoke it using instance.

class Person:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def staticmeth():
        return 'hello'
