N = int(input("How many numbers: "))
total_sum = 0
count_even = 0
count_odd = 0
sum_even = 0
sum_odd = 0
count_negative = 0
count_positive = 0
count_between_50_and_100 = 0

for _ in range(N):
    number = int(input("Enter a number: "))
    total_sum += number  

    if number % 2 == 0:  
        sum_even += number  
        count_even += 1
    else:
        sum_odd += number  
        count_odd += 1

    if number < 0:
        count_negative += 1
    elif number > 0:
        count_positive += 1

    if 50 <= number <= 100:
        count_between_50_and_100 += 1

print("Total Sum of all inputted numbers:", total_sum)  # Output the total sum
print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
print("Number of negative numbers:", count_negative)
print("Number of positive numbers:", count_positive)
print("Numbers between 50 and 100:", count_between_50_and_100)
