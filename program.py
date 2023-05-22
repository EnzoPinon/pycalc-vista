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
            #input number
            first_num = new_ui.numberInput()
            sec_num =  new_ui.numberInput()
            #validate
            num1 = new_ui.numberValidator(first_num)
            num2 = new_ui.numberValidator(sec_num)

            if num1 is 'invalid' or num2 is 'invalid':
                print("one of the inputs are invalid. Please try again.")
            else:
                result = calc.add(num1, num2)
                new_ui.showResults(selection, num1, num2, result)
        if selection is 2:
            #input number
            first_num = new_ui.numberInput()
            sec_num =  new_ui.numberInput()
            #validate
            num1 = new_ui.numberValidator(first_num)
            num2 = new_ui.numberValidator(sec_num)

            if num1 is 'invalid' or num2 is 'invalid':
                print("one of the inputs are invalid. Please try again.")
            else:
                result = calc.subtract(num1, num2)
                new_ui.showResults(selection, num1, num2, result)
        if selection is 3:
            #input number
            first_num = new_ui.numberInput()
            sec_num =  new_ui.numberInput()
            #validate
            num1 = new_ui.numberValidator(first_num)
            num2 = new_ui.numberValidator(sec_num)

            if num1 is 'invalid' or num2 is 'invalid':
                print("one of the inputs are invalid. Please try again.")
            else:
                result = calc.multiply(num1, num2)
                new_ui.showResults(selection, num1, num2, result)
        if selection is 4:
            #input number
            first_num = new_ui.numberInput()
            sec_num =  new_ui.numberInput()
            #validate
            num1 = new_ui.numberValidator(first_num)
            num2 = new_ui.numberValidator(sec_num)

            if num1 is 'invalid' or num2 is 'invalid':
                print("one of the inputs are invalid. Please try again.")
        if selection is 5:
            stop_counter = True
            print("Closing the application. Thank you for using PyCalc Vista!")
        if selection > 5 or selection < 1:
            print("Selection is invalid. Please try again.")