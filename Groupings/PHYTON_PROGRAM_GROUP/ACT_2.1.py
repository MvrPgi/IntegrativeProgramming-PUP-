def calculate_loan_details(area, downpayment_amount, years_to_pay):
    if area < 52.0:
        unit_type, price_per_sqm = "Studio Type", 65892.00
    elif area < 86.5:
        unit_type, price_per_sqm = "2 Bedroom", 58807.00
    else:
        unit_type, price_per_sqm = "3 Bedroom", 53538.00
    
    total_price = area * price_per_sqm
    down_payment_balance = total_price - downpayment_amount
    down_payment_percentage = downpayment_amount / total_price
    discount_percentage = (
        0 if down_payment_percentage < 0.20
        else (0.03 if down_payment_percentage < 0.30
              else (0.04 if down_payment_percentage < 0.40
                    else 0.05))
    )
    discount_amount = total_price * discount_percentage
    
    interest_rate = (
        0.04 if years_to_pay == 5
        else (0.06 if years_to_pay == 10
              else (0.08 if years_to_pay == 15
                    else 0.10))
    )
    interest_amount = total_price * interest_rate
    contract_price = total_price - discount_amount + interest_amount
    monthly_amortization = contract_price / (years_to_pay * 12)
    
    return (unit_type, price_per_sqm, total_price), (down_payment_percentage,downpayment_payment_balance,discount_percentage, discount_amount), (interest_rate, interest_amount, contract_price, monthly_amortization)
area=float(input("Area In Square Meters: "))
down_payment_balance=float(input("Downpayment Amount: ")) # Example down payment percentage
years_to_pay=float(input("Years To Pay: "))

unit_info, discount_info, loan_info = calculate_loan_details(area, down_payment_percentage, years_to_pay)

print("Unit Type:", unit_info[0])
print("Price per Square Meter:", unit_info[1])
print("Total Unit Price:", unit_info[2])

print("\nDown Payment in Percentage:", '{:.0%}'.format(discount_info[0]))
print("Balance:", '{:,.2f}'.format(discount_info[2]))
print("Discount:", '{:.0%}'.format(discount_info[1]))
print("Discount Amount:", '{:,.2f}'.format(discount_info[3]))

print("\nInterest:", '{:.0%}'.format(loan_info[0]))
print("Interest Amount:", '{:,.2f}'.format(loan_info[1]))
print("Contract Price:", '{:,.2f}'.format(loan_info[2]))
print("Monthly Amortization:", '{:,.2f}'.format(loan_info[3]))