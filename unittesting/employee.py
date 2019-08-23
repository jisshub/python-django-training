class Employee:
    pay_raise = 2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}{self.last}@gmail.com"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @property
    def apply_raise(self):
        self.pay = self.pay * self.pay_raise
        return self.pay

# here v use property decorator bfore avery method so v can call them as an attribute.
