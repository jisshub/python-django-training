class One:
    def m1(self):
        print('helo')


class Two(One):
    def m2(self):
        print('hai')


class Three(Two):
    def m3(self):
        print('dad')


# here it is multilevel inheritance since, class two inherit class one.
#  and also class three inherit class two
# whch means that class three can inherit both class one and class two


# Multiple Inheritance

# Multiple Inheritance
# Second Example
# class Three inherit both class two and one.
class One:
    def m1(self):
        print('d')


class Two:
    def m2(self):
        print('a')


class Three(One, Two):
    def m3(self):
        print('sds')


class One:
    def m1(self):
        print('d')


class Two:
    def m1(self):
        print('a')


class Three(One, Two):
    def m3(self):
        print('sds')


class One:
    def m1(self):
        print('d')


class Two:
    def m1(self):
        print('a')


class Three(Two, One):
    def m3(self):
        print('sds')

# here class One and Two hav same methods.
# and class Three inherit both.
# in this case, when instance try to invoke method m1()
# then body of m1 in class Two is printed.
# since it is passed first as an arg.
