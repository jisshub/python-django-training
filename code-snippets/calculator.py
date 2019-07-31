class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculations(self):
        add = self.num1 + self.num2
        sub = self.num2 - self.num1
        mod = self.num1 % self.num2
        div = self.num1 / self.num2
        return f"{add} {sub} {mod} {div}"


c1 = Calculator(10, 5)

