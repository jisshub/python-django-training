class Cars:
    def __init__(self, company):
        self.comp = company


class Car1(Cars):
    def specs(self, model):
        self.model = model

    def func1(self):
        return self.model


class Car2:
    def others(self, price):
        self.price = price
        return self.price


class Car3(Car1, Car2):
    def manage(self):
        insurance = input('Whether insurance or not?(y/n): ')
        return insurance
