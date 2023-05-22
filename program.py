from calculate import Calculator
from interface import UserInterface

calc = Calculator()
new_ui = UserInterface()

stop_counter = False

print("=============================\nPyCalc\n-Vista Edition-\n\nBy EnzoPinon\n=============================\n")

while not stop_counter is True:
    print("\n**Choices**\n(1) Addition [+]\n(2) Subtraction [-]\n(3) Multiplication [*]\n(4) Division [/]\n(5) Close the application\n")
    choice = new_ui.selectionInput()
    selection = new_ui.selectionValidator(choice)

    if selection is 'null':
        print("Input is invalid.")
    
    if not selection is 'null':
        if selection is 1:
            # Addition
        if selection is 2:
            # subtraction
        if selection is 3:
            # multiplication
        if selection is 4:
            # division
        if selection is 5:
            # quit application
        else:
            print("Selection is invalid. Please try again.")