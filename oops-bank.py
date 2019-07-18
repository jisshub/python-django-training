class Bank:
    def __init__(self, name, account_type, balance):
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


customer1 = Bank('Ajith', 'Savings', 40000)




