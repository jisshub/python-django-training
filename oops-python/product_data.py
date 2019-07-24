class Customer:
    def __init__(self, name, cust_id):
        self.name = name
        self.cust_id = cust_id


class Product:
    def purchase(self):
        self.id = 3232
        self.name = 'dadda'
        self.price = 500


class Payment(Customer, Product):
    # purchase_list = []

    def display_prod(self):
        # global purchase_list
        new = [(self.name, self.price)]
        return new



