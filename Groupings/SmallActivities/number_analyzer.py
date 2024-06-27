
class NumberAnalyzer:
    def __init__(self):
        self.largest = 0
        self.smallest = 0
        self.total_sum = 0
        self.count_even = 0
        self.count_odd = 0
        self.sum_odd = 0
        self.sum_even = 0
        self.count_negative = 0
        self.count_positive = 0
        self.In_Range = 0

    def analyze_numbers(self, numbers):
        for number in numbers:
            self.total_sum += number
            if number > self.largest:
                self.largest = number
            else:
                number < self.smallest
                self.smallest = number
            if number % 2 == 0:
                self.count_even += 1
                self.sum_even += number # add previous even number to the number
            else:
                self.count_odd += 1
                self.sum_odd += number # add previous odd number to the number
            if number < 0:
                self.count_negative += 1 # + 1 to count_negative variable
            elif number > 0:
                 self.count_positive +=1 # + 1 to count_positive variable  
            if 50 <= number <= 100:
                self.In_Range += 1 # increment to inRange variable when satisfied
            

    def print_results(self):
        print("________________________________________________")
        print("Total Sum of all inputted numbers:", self.total_sum)
        print("________________________________________________")
        print("Number of even numbers:", self.count_even, "\nNumber of odd numbers:", self.count_odd)
        print("________________________________________________")
        print("Sum of even numbers:", self.sum_even, "\nSum of odd numbers:", self.sum_odd)
        print("________________________________________________")
        print("Number of negative numbers:", self.count_negative, "\nNumber of positive numbers:", self.count_positive)
        print("________________________________________________")
        print("Number of numbers between 50-100:", self.In_Range)   
        print("________________________________________________")
