# OOPS
# Syntax
# class Classname:
#
# class Person:
#
#
#     def speak(self):
#         print('welcome')
#
#
# obj1=Person()


class Student:
    def marks(self):
        a = 10
        b = 20
        print(a + b)


obj2 = Student()
obj3 = Student()


# can create mulitple objects for a class
# here marks is the behaviour or functionality of the objects

# self is used to point to the instance variable
#
# class Employee:
#     def details(self, salary, age):
#         self.salary = salary
#         self.age = age


# Bank Class

class Bank:
    def details(self, bank, minibalance):
        self.bank = bank
        self.minibalance = minibalance

    def deposit(self, account):
        amount = int(input('Enter amount: '))
        self.minibalance += amount

    def withdrawal(self, balance):
        self.minibalance = balance
        withdraw_amt = int(input('Enter amount to withdraw: '))
        self.minibalance -= withdraw_amt

    def bal_enquiry(self, balance):
        self.minibalance = balance

    # def withdrawal(self,minibalance):


class Student:
    def details(self, name, id, college):
        self.stud_name = name
        self.stud_id = id
        self.college = college

    def display(self):
        print('Student Name: ', self.stud_name)
        print('ID: ', self.stud_id)
        print('college: ', self.college)


class Bank:
    def account_details(self, holder_name, account_type, balance, max_amount, min_amount):
        self.name = holder_name
        self.type = account_type
        self.balance = balance
        self.max_amt = max_amount
        self.min_amt = min_amount

    def deposit(self):
        amount = int(input('Amount: '))
        if amount < self.max:
            self.bal += amount
            print(self.bal)
        else:
            print('Amount Exceeded')

    def withdrawal(self, min_amount):
        print('Current Balance:', self.bal)
        amount = int(input('Amount: '))

        if amount < self.min:
            self.bal -= amount
            print(self.bal)
        else:
            print('min_amount exceeded')
