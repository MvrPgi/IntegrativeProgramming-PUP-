
class BillOrder:
    def __init__(self):
        self.price = 0

    def out(self, pizza):
        pizza.compute_price()
        self.price = pizza.price
        price_formatted = "{:.2f}".format(self.price)
        print(f"You ordered for {pizza.toppings} Pizza with the size of {pizza.diameter * 2.54:.2f} centimeter for PHP{price_formatted}.")
        print("Amount Due:", price_formatted)

    def get_price(self):
        return self.price
