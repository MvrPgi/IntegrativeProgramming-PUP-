drink = 15
sandwich = 25

num_drink = int(input("ilang drinks lods? "))
num_wich = int(input("ilang sandwich pu? "))

total_bill = (num_drink * drink) + (num_wich * sandwich)
payment = int(input("Enter your payment: "))
change = payment - total_bill

if payment >= total_bill:
    print(f"Your total bill is {total_bill} and your change is {change}.")
else:
    print("kulang po bayad nyo huhu ;((")