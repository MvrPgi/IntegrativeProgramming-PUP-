area = float(input("Area In Square Meters: "))
downpayment_amount = float(input("Downpayment Amount: ")) 
years_to_pay = float(input("Years To Pay: "))

if area < 52.0:
    unit_type, price_per_sqm = "Studio Type", 65892.00
elif area < 86.5:
    unit_type, price_per_sqm = "2 Bedroom", 58807.00
else:
    unit_type, price_per_sqm = "3 Bedroom", 53538.00

total_price = area * price_per_sqm
down_payment_percentage = (downpayment_amount / total_price) * 100

if down_payment_percentage < 20:
    discount_rate = 0
elif down_payment_percentage < 30:
    discount_rate = 3
elif down_payment_percentage < 40:
    discount_rate = 4
else:
    discount_rate = 5

discount_amount = (discount_rate / 100) * total_price

if years_to_pay == 5:
        interest_rate = 0.04
elif years_to_pay == 10:
        interest_rate = 0.06
elif years_to_pay == 15:
        interest_rate = 0.08
else:
        interest_rate = 0.10

interest_amount = total_price * interest_rate
contract_price = total_price - discount_amount + interest_amount
monthly_amortization = contract_price / (years_to_pay * 12)

print("\nUnit Type:", unit_type)
print("Price per Square Meter:", price_per_sqm)
print("Total Unit Price:", total_price)

print("\nDown Payment in Percentage:", '{:.0f}%'.format(down_payment_percentage))
print("Discount Rate:", '{:.0f}%'.format(discount_rate))
print("Discount Amount:", '{:,.2f}'.format(discount_amount))

print("\nInterest Rate:", '{:.0f}%'.format(interest_rate * 100))
print("Interest Amount:", '{:,.2f}'.format(interest_amount))
print("Contract Price:", '{:,.2f}'.format(contract_price))
print("Monthly Amortization:", '{:,.2f}'.format(monthly_amortization))
