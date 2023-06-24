
def calc():
    while True:
        print()
        print('MPG Calculator')
        print('by: Logan Dye')
        print()
        print('Please enter your vehicles average miles per gallon: ', end=" ")
        mpg = float(input())
        print()
        print('Please enter the price of gas per gallon: ', end=" ")
        price = float(input())
        print()
        print('How many miles is your trip? ', end=" ")
        miles = float(input())
        print()
        total_cost = (miles / mpg) * price
        print(f'The total for cost for driving {int(miles)} miles is ${total_cost:.2f}.')
        print()
        print('Would you like to try another? ', end=" ")
        if input() == 'yes':
            continue
        else: 
            break
        
