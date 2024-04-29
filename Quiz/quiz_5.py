from take_order import TakeOrder
def main():
    while True:
       
        take_order = TakeOrder()
        take_order.take_order()
        response = input("Do you want to place another order? (Y/N): ")
        if response.upper() != 'Y':
            break


if __name__ == "__main__":
    main()
