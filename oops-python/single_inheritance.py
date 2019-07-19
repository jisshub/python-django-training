class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} and age is {self.age}"


class Student(Person):
    def exam(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2


# example 2
class Person:
    def details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} and age is {self.age}"


class Student(Person):
    school = "luminar"

    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2

    def calc(self):
        total = self.mark1 + self.mark2
        return total


# Employee

class Employee:
    def details(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name


class admin(Employee):
    def __init__(self, location, experience):
        self.loc = location
        self.exp = experience

    def display(self):
        return f"{self.loc} and {self.exp}"



