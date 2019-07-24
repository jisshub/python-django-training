def sort_student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


sort_student(name='Ajith', no=33)


# sorting student based on total marks.

class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total = total_marks

    def __repr__(self):
        return self.name


s1 = Student('jiss', '300')
s2 = Student('ajith', '250')
std = [s1, s2]
for each in sorted(std, key=lambda k: k.total):
    print(each)




