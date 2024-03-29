
from number_analyzer import NumberAnalyzer

analyzer = NumberAnalyzer()
N = int(input("How many numbers: "))
numbers = [int(input("Enter a number: ")) for _ in range(N)]
analyzer.analyze_numbers(numbers)
analyzer.print_results()
