class Calculator:
    def divide(self, a, b):
        return a / b
    
    def calculate_average(self, numbers):
        total = sum(numbers)
        count = len(numbers)
        return total / count
    
    def get_percentage(self, value, total):
        return (value / total) * 100
    
    def parse_number(self, text):
        return int(text)
    
    def safe_divide(self, numerator, denominator):
        result = numerator / denominator
        return round(result, 2)