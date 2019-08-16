class Electronics:
    def __init__(self, keyboards, drivers, max_price):
        self.k = keyboards
        self.d = drivers
        self.b = max_price

    def check_keyboard(self):
        if self.b in self.k:
            self.k.remove(self.b)

    def check_drivers(self):
        if self.b in self.d:
            self.k.remove(self.b)
        # return display()

    def display(self, price=None):
        if price is None:
            price = []
        # self.price = price
        for each in self.k:
            for each2 in self.d:
                total = each + each2
                if total <= self.b:
                    price.append(total)
        return max(price)


e1 = Electronics([40, 50, 60], [5, 8, 12], 60)
e1.check_keyboard()
e1.check_drivers()
e1.display()
