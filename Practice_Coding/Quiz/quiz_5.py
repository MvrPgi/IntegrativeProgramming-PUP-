from take_order import TakeOrder
def main():
    while True:
       
        take_order = TakeOrder()
        take_order.take_order()
        response = input("Do you want to place another order? (Y/N): ")
        if response.upper() == 'Y':
            continue       
        elif response.upper() == 'N':
            print("Thank you for using our system. Have a great day!")
            break


if __name__ == "__main__":
    main()
