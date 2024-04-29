
#m   Studio Type  P65, 892.00 per sqm
#52.0 sqm to below 86.5 sqm   2 Bedroom    P58, 807.00 per sqm
#86.5 sqm and above           3 Bedroom    P53, 380.00 per sqm
#*sqm = square meter

#Down payment (in Pesos)
#Discount is given if down payment is
#Below 20%                    No Discount
#20% -                        Below 30% 3% discount
#30% -                        Below 40% 4% discount
#40% -                        and above 5% discount
#Years to pay(in number of years)
#5                            Years 4% Interest
#10                           Years 6% Interest
#15                           Years 8% Interest
#20                           Years 10% Interest

# Unit Type, Price per Square Meter and Total Unit Price
# Down Payment in Percentage, Discount and Discount Amount
# Interest, Interest Amount, Contract Price, Monthly Amortization

def area():
  area=float(input("Area In Square Meters: "))
  studio = ("Studio Type")
  bed = (" 2 Bed Room")
  bed2 ="3 Bed Room,"
  P1 = 65892.00*area
  P2 = 58807.00*area
  P3 = 53380.00*area

  if area < 52.0:
    print("Unit Type: ",studio) 
    print(f"Total Price: P{P1}") 
    return P1
  elif  area  <= 86.7:
    print("Unit Type: ",bed)
    print(f"Total Price P{P3}")
    return P2
  elif area <= 86.5:
    print("Unit Type: ",bed2) 
    print(f"Total Price: P{P2}") 
    return P3
    

def downpayment(total_price):
  downpayment=float(input("Downpayment Amount: "))
  if downpayment < 0.2 * total_price:
        print("No discount applied.")
  elif 20 <= downpayment < 30:
        print("3% discount applied.")
  elif 30 <= downpayment < 40:
        print("4% discount applied.")
  else:
        print("5% discount applied.")
  print(f"BALANCE {total_price - downpayment}:")




area()
downpayment()

