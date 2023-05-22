class Calculator:
    
    def add(self, num1, num2):
        sum = num1 + num2
        return sum
    
    def subtract(self, num1, num2):
        diff = num1 - num2
        return diff
    
    def multiply(self, num1, num2):
        produce = num1 * num2
        return produce
    
    def divide(self, num1, num2):
        try:
            quotient = num1 / num2
            return quotient
        except ZeroDivisionError:
            quotient = 'error'
            return quotient