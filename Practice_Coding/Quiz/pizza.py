class Pizza:
    def __init__(self):
        self.toppings = ""
        self.diameter = 0
        self.how_many = 0
        self.discount = ""
        self.price = 0.0

    def set_toppings(self, toppings):
        self.toppings = toppings

    def set_diameter(self, diameter):
        self.diameter = diameter

    def set_how_many(self, how_many):
        self.how_many = how_many

    def set_discount(self, discount):
        self.discount = discount

    def compute_price(self):
        toppings_price = 0
        if self.toppings == "Pepperoni":
            toppings_price = 100
        elif self.toppings == "Ham and Cheese":
            toppings_price = 150
        elif self.toppings == "Hawaiian":
            toppings_price = 200

        diameter_cm = self.diameter * 2.54
        self.price = (toppings_price + (5 * diameter_cm)) * self.how_many

        if self.discount == "Senior Citizen":
            self.price *= 0.85
        elif self.discount == "VIPCard":
            self.price *= 0.88

