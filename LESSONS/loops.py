N = int(input("How many numbers: "))
largest = float('-inf')
smallest = float('inf')

for x in range(N):
    number = int(input("Enter a number: "))
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("The largest value is:", largest)
print("The smallest value is:", smallest)