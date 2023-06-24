from mpg_calc import calc
from smpl_intr import simple_interest_calculator
import sys

    
print()
print('\tINTERACTIVE CALCULATOR')
print()
print('by: Logan Dye')
print()
print('Hello! \n\tWhich calculator program would you like to use? ')
print('Hint: Type options to view the calculator choices')
while True:
    options = ['MPG Calculator', 'Interest Calculator']
    user_selection = input()
    if user_selection == 'options':
        print('\t', end='')
        print(*options, sep=', ')
    elif user_selection == 'Interest':
        while True:
            print('Simple or Compound?')
            interest_choice = input()
            if interest_choice == 'Simple':
                simple_interest_calculator()
                break
            elif interest_choice == 'Compound':
                print('That feature is not available yet.')
            elif interest_choice == 'back':
                break
            else:
                print()
                print('Not a valid response. \n Enter back to go to the main menu.')
    elif user_selection == 'MPG Calculator':
        calc()
    elif user_selection == 'exit':
        sys.exit()
    else:
        print('Please enter a valid command.')



