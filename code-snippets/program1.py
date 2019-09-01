# inheritance
# ---------------------
class Phone:
    # price = 0
    # discount = 0

    def __init__(self, camera, brand):
        self.camera = camera
        self.brand = brand


class Price(Phone):
    def PriceDetail(self):
        if self.camera:
            self.price = 45000
        else:
            self.price = 20000
        return self.price


class CashBack(Price):
    def CashBackDetails(self):
        if self.price == 45000:
            discount = self.price * .20
        else:
            discount = self.price * .10
        return discount
