from pizza import Pizza
from bill_order import BillOrder

class TakeOrder:
    def __init__(self):
        self.pie = Pizza()
    def display_options(self):
        print("Possible Toppings:")
        print("- Pepperoni")
        print("- Ham and Cheese")
        print("- Hawaiian")

        print("\nPossible Discounts:")
        print("- Senior Citizen")
        print("- VIPCard")

    def take_order(self):
        self.display_options()

    def take_order(self):
        self.display_options()
        self.pie.set_toppings(input("Enter Toppings: "))
        self.pie.set_diameter(int(input("Enter Diameter in inches: ")))
        self.pie.set_how_many(int(input("Enter How Many?: ")))
        self.pie.set_discount(input("Enter Type of Discount: "))

        bill_order = BillOrder()
        bill_order.out(self.pie)

        amount_due = bill_order.get_price()
        amount_received = 0

        while amount_received < amount_due:
            amount_received = float(input("Enter amount received: "))
            if amount_received < amount_due:
                print("Insufficient amount. Please enter a higher amount.")


        change = amount_received - amount_due
        print("Change:", "{:.2f}".format(change))