class Cars:
    company = 'Toyoto'

    def __init__(self, model, variant):
        self.model = model
        self.variant = variant

    def specifications(self, fuel_type, seating_capacity):
        self.fuel = fuel_type
        self.seats = seating_capacity


c1 = Cars('Glanza', 'blue orange')

# here instance method is specifications
