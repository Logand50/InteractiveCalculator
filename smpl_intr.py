
def simple_interest_calculator():
    while True: 
        print()
        print('Simple Interest Calculator')
        print('by: Logan Dye')
        print()
        print('Enter the ammount initially invested: ', end= ' ')
        principal = float(input())
        print('Enter the interest rate: ', end=' ')
        interest = float(input())
        print('Enter the length of the investment in years: ', end=' ')
        length = float(input())
        print()
        end_total = principal * (interest / 100) * length + principal
        print(f'After {length} years your investment of ${principal} will have grown into ${end_total:.2f}!')
        print()
        print('Would you like me to break that down more you you?')
        if input() == 'yes':
            print()
            i = 0
            while i < length:
                i = i + 1
                years_total = (principal * (interest / 100) * i) + principal
                print(f'Year {i} your total savings would be ${years_total:.2f}.')
        else:
            break
        print('Would you like to restart the Simple Interest Calculator?')
        if input() == 'yes':
            continue
        else:
            break
