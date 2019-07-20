class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + self.last + '@' + 'gmail.com'

    def full_name(self):
        return f"{self.first} {self.last}"


emp1 = Employee('jissmon', 'jose')


# so here if v explicitly change the first attribute
# ie emp1.first='kumar'
# and later do,
#     emp1.email -- it doesnt modify the first attribute
# bt does emp1.full_name()
#     --- it gives the modified first attrbiute as the result
# since while full_name() is invoked, it takes the latest change made to the attributes.
# so inorder to update the email automatically when made changes to the first and last attributes.


# v acn solve it by defining a new func called new-email and repeat the code to set the email
# as given in the init method.
# so it is not a good idea.
# given below--
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + self.last + '@' + 'gmail.com'

    def full_name(self):
        return f"{self.first} {self.last}"

    def new_email(self):
        self.email = self.first + self.last + '@' + 'gmail.com'
        return f"{self.email}"


emp1 = Employee('jissmon', 'jose')


# So here v use Property Decorator to resolve this
# it allows us to define a method and can access that method like an attribute.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = self.first + self.last + '@' + 'gmail.com'

    @property
    def email(self):
        return f"{self.first}{self.last}" + '@' + 'gmail.com'

    def full_name(self):
        return f"{self.first} {self.last}"


emp1 = Employee('jissmon', 'jose')

# here v make an another instance methd called email and set the email in it.
# and v place property decorator above the method.
# and v can invoke this method as an attributes. ie..
#     emp1.email
