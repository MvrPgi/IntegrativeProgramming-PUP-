
class NumberAnalyzer:
    def __init__(self):
        self.total_sum = 0
        self.count_even = 0
        self.count_odd = 0
        self.sum_odd = 0
        self.sum_even = 0
        self.count_negative = 0
        self.count_positive = 0
        self.count_between_50_and_100 = 0

    def analyze_numbers(self, numbers):
        for number in numbers:
            self.total_sum += number
            if number % 2 == 0:
                self.count_even += 1
                self.sum_even += number
            else:
                self.count_odd += 1
                self.sum_odd += number
            if number < 0:
                self.count_negative += 1
            elif number > 0:
                self.count_positive +=1
            if 50 <= number <= 100:
                self.count_between_50_and_100 += 1

    def print_results(self):
        print("Total Sum of all inputted numbers:", self.total_sum)
        print("Number of even numbers:", self.count_even, "\nNumber of odd numbers:", self.count_odd)
        print("Sum of even numbers:", self.sum_even, "\nSum of odd numbers:", self.sum_odd)
        print("Number of negative numbers:", self.count_negative, "\nNumber of positive numbers:", self.count_positive)
        print("Numbers between 50 and 100:", self.count_between_50_and_100)
