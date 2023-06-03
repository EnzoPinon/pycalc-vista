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
    
    