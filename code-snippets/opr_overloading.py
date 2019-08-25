class Operator:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, other):
        return self.num1 + other.num1

# op1 = Operator(33)
# op2 = Operator(31)
# print(op1 + op2)
# 64
