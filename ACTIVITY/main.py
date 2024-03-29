
from number_analyzer import NumberAnalyzer

analyzer = NumberAnalyzer()
N = int(input("How many numbers: "))
numbers = [int(input(f"Enter a number: [{i+1}]")) for i in range(N)]
analyzer.analyze_numbers(numbers)
analyzer.print_results()
