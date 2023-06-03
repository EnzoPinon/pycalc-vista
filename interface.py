class UserInterface:
    def selectionValidator(self, choice):
        try:
            selection = int(choice)
            return selection
        except ValueError:
            selection = 'null'
            return selection 

    def selectionInput(self):
        print("\n**Choices**\n(1) Addition [+]\n(2) Subtraction [-]\n(3) Multiplication [*]\n(4) Division [/]\n(5) Powering (a raised to b)\n(6) rooting (nth root of a)\n(7) compute for all methods\n(8) Close the application\n")
        choice = input("Please select the number of you choice: ")
        return choice
    
    def numberInput(self):
        first_number = input("Please insert your two numbers: ")
        return first_number
    
    def numberValidator(self, first_number):
        try:
            num1 = float(first_number)
            return num1
        except ValueError:
            num1 = 'invalid'
            return num1
        
    def showResults(self, selection, num1, num2, result):
        print("============================================")
        print("-Results-\n\n")
        if selection is 1:
            print("Method: Addition\n")
        if selection is 2:
            print("Method: Subtraction\n")
        if selection is 3:
            print("Method: Multiplication\n")
        if selection is 4:
            print("Method: Division\n")
        if selection is 5:
            print("Method: Powering (n raised to nth)")
        if selection is 6:
            print("Method: rooting (nth root of n)")
        print("First number: ", num1, "\n")
        print("Second number: ", num2, "\n")
        print("Result: ", result, "\n\n")
        print("============================================\n\n")
        print("Calculation complete! Thank you for using PyCalc Vista!")
    
    def print_all(self, num1, num2, sum, diff, product, quotient, nth_root, result):
        if quotient is 'error' or nth_root is 'error':
            return print("You may have given a negative input that isn't allowed by nth rooting or divided by zero. Please try again.")
        else:
            print("============================================")
            print("-Results-\n\n")
            print("Method: ALL METHODS")
            print("First number: ", num1, "\n")
            print("Second number: ", num2, "\n")
            print("Sum: ", sum, "\n")
            print("Difference: ", diff, "\n")
            print("Product: ", product, "\n")
            print("Quotient: ", quotient, "\n")
            print("Powered to nth: ", result, "\n")
            print("nth root of n: ", nth_root, "\n\n")
            print("============================================\n\n")
            print("Calculation complete! Thank you for using PyCalc Vista!")
