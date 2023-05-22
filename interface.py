class UserInterface:
    def selectionValidator(self, choice):
        try:
            selection = int(choice)
            return selection
        except ValueError:
            selection = 'null'
            return selection 

    def selectionInput(self):
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
        print("First number: ", num1, "\n")
        print("Second number: ", num2, "\n")
        print("Result: ", result, "\n\n")
        print("============================================\n\n")
        print("Calculation complete! Thank you for using PyCalc Vista!")
