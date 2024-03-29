
from number_analyzer import NumberAnalyzer
#1. output the sum of all the inputted numbers
#2. output how many numbers are even numbers and odd numbers
#3. output the sum of all even numbers and sum of all odd numbers
#4. output how many numbers are negative numbers and positive numbers
#5.output how many of the inputted numbers are between 50 - 100

analyzer = NumberAnalyzer()
N = int(input("How many numbers: "))
numbers = [int(input(f"Enter a number: [{i+1}]")) for i in range(N)]
analyzer.analyze_numbers(numbers)
analyzer.print_results()
