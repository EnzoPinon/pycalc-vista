class UserInterface:
    def selectionValidator(self, choice):
        try:
            selection = int(choice)
            return selection
        except:
            selection = 'null'
            return selection 