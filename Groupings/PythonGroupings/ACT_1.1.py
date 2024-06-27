print("MATERIALS")
print("----------------------------------------")
print("ENTER THE COST OF THE FOLLOWING")

Ppaper = float(input("Paper:    "))
Ppencil = float(input("Pencil:   "))
Sscissors = float(input("Scissors: "))
Eeraser = float(input("Eraser:   "))

print("PURCHASE")
print("----------------------------------------")
print("HOW MANY ITEMS OF THE FOLLOWING DID YOU BUY")

paper = float(input("Paper:    "))
pencil = float(input("Pencil:   "))
scissors = float(input("Scissors: "))
eraser = float(input("Eraser:   "))
price = (paper*Ppaper)+(pencil*Ppencil)+(scissors*Sscissors)+(Eeraser*eraser)
no_items= paper+pencil+scissors+eraser

print(f"THE TOTAL PRICE IS        :           P{price}")
print(f"NO OF ITEMS               :            {no_items}")
vat_rate = 0.12
vat_amount = price * vat_rate
total_before_vat = price - vat_amount
print(f"PRICE BEFORE THE VAT      :            {total_before_vat}")
print(f"VAT 12%                   :            {vat_amount}")

