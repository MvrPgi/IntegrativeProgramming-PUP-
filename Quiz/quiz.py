side1 = int(input("Enter the length of side 1: "))  # Input for the length of side 1
side2 = int(input("Enter the length of side 2: "))  # Input for the length of side 2
side3 = int(input("Enter the length of side 3: "))  # Input for the length of side 3

if side1 == side2 == side3:
    print("Equilateral triangle")  # If all sides have the same length
elif (side1==side2) or (side1==side3) or (side2==side3):
    print("Isosceles triangle")  # If only two sides have the same length
elif (side1!=side2) and (side2!=side3) and (side1!=side3):
    print("Scalene triangle")  # If no sides have the same length
