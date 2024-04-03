   Commission
# 1         7% Of Sale Or P400 Whichever is More
# 2         10% Of Sale Or P900 Whichever is Less
# 3         12% Of Sale
# 4         P250 Regardless Of Sale Price
# Make A Program That Will Input Type Of Application Sold 1-4 and the sale price and what would be the output of commision

def calculate_commission(appliance_type, sale_price):
    if appliance_type == 1:
        commission = max(0.07 * sale_price, 400)
    elif appliance_type == 2:
        commission = min(0.10 * sale_price, 900)
    elif appliance_type == 3:
        commission = 0.12 * sale_price
    elif appliance_type == 4:
        commission = 250
    else:
        print("Invalid appliance type")
        return None
    return commission

def main():
    print("Welcome to the Household Appliances Commission Calculator!")
    while True:
        appliance_type = int(input("Enter the type of appliance sold (1-4):  "))
        sale_price = float(input("Enter the sale price: "))
        
        commission = calculate_commission (appliance_type, sale_price)
        if commission is not None:
            print("Your commission:  P", commission)
        

    main()