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