#Write a program to accept the price per unit of the following items:
#Paper, Pencil, Scissors and Eraser
#For Example:
#Paper = P1.00
#Pencil = P5.00
#Scissors = P25.00
#Eraser = P2.50

#Then accept the number of unit(s) bought per item:
#For example:
#10 Sheets of Paper
#3 Pieces of Pencil
#1 Pair of Scissors
#1 Piece of Eraser
#Display Total Amount Due.
#Accept Cash Amount Given by Customer.


# PRINT THE PRICE 
print("MATERIALS")
print("-----------")
print("ENTER THE COST OF THE FOLLOWING")
print("\nPAPER = 1\nPENCIL = 5\nSCISSORS = 25\nERASER = 2.50")
print("\nPURCHASE")
print("-----------")
print("HOW MANY ITEMS OF THE FOLLOWING DID YOU BUY")

#GIVEN PRICE VARIABLE
ppaper = 1
ppencil = 5
sscissors = 25
eeraser = 2.50


# INPUT VARIABLE
paper = float(input("PAPER :  "))
pencil = float(input("PENCIL :  "))
scissors = float(input("SCISSORS :  "))
eraser = float(input("ERASER :  "))

#FORMULA FOR TOTAL PRICE AND NO OF ITEMS
output = (paper*ppaper)+(pencil*ppencil)+(scissors*sscissors)+(eeraser*eraser)
No_items= paper+pencil+scissors+eraser


#PRINT THE FORMULA VARIABLE
print(f"THE TOTAL PRICE IS:P {output}")
print(f"NO OF ITEMS:  {No_items}")

# INPUT PAYMENT AND FORMULA FOR CHANGE
payment = float(input("Enter Cash:P "))
change = payment-output
print(f"P{change}")

# PRICE BEFORE THE VAT

#PRICE AFTER THE VAT

# OUTPUT 2