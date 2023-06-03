from calculate import Calculator
import math

class pycalc(Calculator):
    def powered(self, num1, num2):
        result = num1 ** num2
        return result
    
    def rooted(self, num1, num2):
        try:
            result = num1 ** 1/num2
            return result
        except ValueError:
            result = 'error'
            return result
    
    def calculate_all(self, num1, num2):

        try:
            quotient = num1 / num2
            
        except ZeroDivisionError:
            quotient = 'error'
        
        try:
            nth_root = num1 ** 1/num2
        except ValueError:
            nth_root = 'error'
        
        sum = num1 + num2
        diff = num1 - num2
        product = num1 * num2
        return quotient, nth_root, sum, diff, product
