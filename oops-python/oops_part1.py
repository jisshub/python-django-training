# here v create a class Employee
# created a special method init which will be called automatically when v create an instance.
# if v dont use init method v need to manually set the attributes for each instance variables
# for example:
#     emp1.first='Corey'
#     emp1.last='Schafer
# here emp1.first, emp1.last r the instance variables.
# so v creata init method with
# so if v use init method v can pass all the attributes as an argument when v create the instance.

# here the parameter self in each methods automatically receives the instance when it is created.
# or v can say instance is passed automatically to parameter self. ie self points to that particular instance.
# then v can specify other parameters in init method.

# later v can assign attributes or parameters to each instance variable
# example:
#     self.first=first
#     self.last=last
# here self.first and self.last r the instance variables.

# class Employee:
#     def __init__(self, first, last, salary):
#         self.first = first
#         self.last = last
#         self.salary = salary
#         self.email = self.first + self.last + '@' + 'gmail.com'
#
#     def display(self):
#         print(self.email)
#         print(self.salary)
#         amount = self.salary
#         print(amount)


class Player:
    def __init__(self, name, position, curr_skill_per):
        self.name = name
        self.position = position
        self.curr_skill_per = curr_skill_per

    def status(self):
        matches_played = int(input('Enter no of matches: '))
        if matches_played > 10:
            self.curr_skill_per += (self.curr_skill_per * matches_played) / 100
            print(self.curr_skill_per)
        else:
            self.curr_skill_per -= (self.curr_skill_per * matches_played) / 100
            print(self.curr_skill_per)

    def full_data(self):
        print(self.name, self.position, self.curr_skill_per)


player1 = Player('Hazard', 'LW', 70)


class Identity:
    dict = {}

    def __init__(self, names, args):
        self.names = names
        self.id = args

    def assign(self):
        for name in self.names:
            for id in self.id:
                # update the dictionary
                dict.update({name: id})

        return dict


id1 = Identity(['jiss', 'jose'], [34, 54, 76])

data = [3, 4, 5]
names = ['j', 'a', 'c']
for each in data:
    for name in names:
        print(f'{each}: {name}')



