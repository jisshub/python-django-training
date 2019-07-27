class Bank:
    bankname = 'SBT'

    def details(self, name, account_type, balance):
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.max_amt = 10000
        self.min_amt = 20000

    def deposit(self):
        amount = int(input('Amount: '))
        if amount < self.max_amt:
            self.balance += amount
            return self.balance
        else:
            print('Amount Exceeded')

    def withdrawal(self):
        print('Current Balance:', self.balance)
        amount = int(input('Amount: '))

        if amount < self.min_amt:
            self.balance -= amount
            return self.balance
        else:
            print('min_amount exceeded')


customer1 = Bank()

#
# class Student:
#     college_name = 'FISAT'
#     names = []
#
#     def basic_details(self, name, marks1, marks2):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#
#     def sort_all(self):
#
#         names.append(self.name)
#         names.sort()
#         return names
#
#     def average(self):
#         average = (self.marks1 + self.marks2) / 2
#         return average
#
#     def grade(self):
#         if (self.marks1 + self.marks2) > 90:
#             return 'Grade A'
#
#         elif (self.marks1 + self.marks2) < 90 and (self.marks1 + self.marks2) > 70:
#             return 'Grade B'
#         else:
#             return 'Grade C'
#
#     def display(self):
#         print(Student.college_name)
#
#
# ajith = Student()
# # ajith.basic_details('dbks', 40, 50)
