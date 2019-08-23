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

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


emp1 = Employee('jissmon', 'jose')


# here v make an another instance methd called email and set the email in it.
# and v place property decorator above the method.
# and v can invoke this method as an attributes. ie..
#     emp1.email


# we can also add this property decrorator to full_name method and can invoke it as an attribute.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first} {self.last}" + '@' + 'gmail.com'

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


emp1 = Employee('Aju', 'asd')
emp1.full_name = 'Jissmon Jose'


# here v cannot set the values to the full name when it is invoked as an attribute.
# ie. emp1.full_name='jidda asdas'
# to set the values for the attribute, v use setter.


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first} {self.last}" + '@' + 'gmail.com'

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first = name.split()[0]
        self.last = name.split()[1]
        return f"{self.first} {self.last}"


emp1 = Employee('Aju', 'asd')


# here setter for the full_name method is, @full_name.setter
# now v can set the value for the full_name while it is invoked.
# here, name parameter receives the value v set for the full_name.
# eg:emp1.full_name='jissmon jose'
# here value 'jissmon jose' is passed to the name parameter.

# since v set the first and last attribute even when v print the email,
# changes also reflected to it.


# Deleter
# if want to delete the fullname,
# so v set the decorator deleter.
# later v can delete that full_name attribute.
# by the way, to delete an attribute use, del keyword

#          ie. del instance.attribute


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}{self.last}" + '@gmail.com'

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first = name.split()[0]
        self.last = name.split()[1]
        return f"{self.first} {self.last}"

    @full_name.deleter
    def delete_name(self):
        print('deleted fullname')
        self.first = None
        self.last = None


emp1 = Employee('Ajith', 'Kumar')

# once we deleted full_name always assign None value to instance variable self.first and self.last
# else if again v invoke full_name attribute, the name will be printed.


# Practice
import re


class Product:
    brand_name = 'Sony'

    def __init__(self, item, model, model_no):
        self.item = item
        self.model = model
        self.model_no = model_no
        # self.modelnumber = self.model + str(modelnumber)

    @property
    def model_mod(self):
        return self.model + str(self.model_no)

    @model_mod.setter
    def change_mod(self, mdname):
        pattern = re.compile(r'\d{3,}')
        self.model_no = pattern.search(mdname).group()
        pattern = re.compile(r'\D{3,}')
        self.model = pattern.search(mdname).group()

    @model_mod.deleter
    def delete_mod(self):
        self.model=None
        self.model_no=None
        return 'model details removed'

    def display(self):
        return f"item: {self.item}, model: {self.model}, modelno: {self.model_no}"


p1 = Product('Headphone', 'MDRX', 745)
