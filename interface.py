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