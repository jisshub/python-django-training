# Stack Operation in Python

class Stack:

    def __init__(self, size):
        self.stack_size = size
        self.empty = list()
        self.top = 0

    def push(self):
        # top = 0
        while self.top < self.stack_size:
            num = int(input('Number:'))
            self.empty.insert(self.top, num)
            self.top += 1
        if self.top >= self.stack_size:
            print('stack full')

    def pop(self):
        if self.empty != list():
            self.empty.pop()
            self.top -= 1
        else:
            print('Empty Stack')

    def display(self):
        return self.empty


s1 = Stack(3)
