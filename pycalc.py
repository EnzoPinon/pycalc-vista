from calculate import Calculator
from interface import UserInterface

ui = UserInterface()

class pycalc(Calculator):
    def powered(self, num1, num2):
        try:
            result = num1 ** num2
            return result
        except ZeroDivisionError:
            result = 'error'
            return result
    
    def rooted(self, num1, num2):
        try:
            result = num1 ** (1.0/num2)
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
            nth_root = num1 ** (1.0/num2)
        except ValueError:
            nth_root = 'error'
        
        sum = num1 + num2
        diff = num1 - num2
        product = num1 * num2
        try:
            result = num1 ** num2
        except ZeroDivisionError:
            result = 'error'
        ui.print_all(num1, num2, sum, diff, product, quotient, nth_root, result)
