from calculate import Calculator
from interface import UserInterface

calc = Calculator()
new_ui = UserInterface()

stop_counter = False

print("=============================\nPyCalc\n-Vista Edition-\n\nBy EnzoPinon\n=============================")

while not stop_counter is True:
    print("**Choices**\n(1) Addition [+]\n(2) Subtraction [-]\n(3) Multiplication [*]\n(4) Division [/]\n(5) Close the application")
    choice = new_ui.selectionInput()
    selection = new_ui.selectionValidator(choice)