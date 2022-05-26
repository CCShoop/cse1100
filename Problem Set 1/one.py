'''Written by Cael Shoop. Soda Dispenser program.'''


def soda_check(soda):
    # Checks if the input value exists, also allowing lowercase
    if soda != '1A' and soda != '1B' and soda != '2A' and soda != '2B' and soda != '2C' and soda != '3A' and soda != '4A' and soda != '5A' and soda != '6A' and soda != '7A' and soda != '1a' and soda != '1b' and soda != '2a' and soda != '2b' and soda != '2c' and soda != '3a' and soda != '4a' and soda != '5a' and soda != '6a' and soda != '7a':
        return False
    return True


def soda_select(soda):
    # Converts soda to the soda name from the input value
    if soda == '1A' or soda == '1a':
        return 'Pepsi'
    elif soda == '1B' or soda == '1b':
        return 'Diet Pepsi'
    elif soda == '2A' or soda == '2a':
        return 'Coca Cola'
    elif soda == '2B' or soda == '2b':
        return 'Diet Coke'
    elif soda == '2C' or soda == '2c':
        return 'Coke Zero'
    elif soda == '3A' or soda == '3a':
        return 'Dr. Pepper'
    elif soda == '4A' or soda == '4a':
        return 'Diet Dr. Pepper'
    elif soda == '5A' or soda == '5a':
        return 'Sprite'
    elif soda == '6A' or soda == '6a':
        return '7-Up'
    elif soda == '7A' or soda == '7a':
        return 'Ginger Ale'


def main():
    # The program creates coins and soda to utilize user input
    coins = 0.00
    soda = ''
    # Accepts user's soda choice
    while not soda_check(soda):
        print('Every soda is $1.00. What soda would you like?')
        print('\t1A. Pepsi')
        print('\t1B. Diet Pepsi')
        print('\t2A. Coca Cola')
        print('\t2B. Diet Coke')
        print('\t2C. Coke Zero')
        print('\t3A. Dr. Pepper')
        print('\t4A. Diet Dr. Pepper')
        print('\t5A. Sprite')
        print('\t6A. 7-Up')
        print('\t7A. Ginger Ale')
        soda = input('Selection: ')
        # Prints an error if user makes an invalid selection
        if not soda_check(soda):
            print('Selection invalid.\n')
    soda = soda_select(soda)
    # A while loop keeps the program accepting coins
    while (coins < 1):
        # An input check to confirm input value is one of the designated values
        new_coins = 0
        while (new_coins != 0.05 and new_coins != 0.10 and new_coins != 0.25):
            new_coins = round(float(input('Insert coins (0.05, 0.10, 0.25): ')), 2)
            # If the value is not accepted, print an error message
            if new_coins != 0.05 and new_coins != 0.10 and new_coins != 0.25:
                print('Value not accepted. Please enter 0.05, 0.10, or 0.25.')
        # If the value is accepted, add it to the count
        coins = coins + new_coins
        coins = round(coins, 2)
        print('Accepted: $' + str(coins))
    # If the value is overpaid, this gives the user their change
    if coins > 1:
        coins = coins - 1.00
        coins = round(coins, 2)
        print('Change: $' + str(coins))
    # The program remembers what soda the user selected and dispenses it
    print(f'Here is your {soda}!')



if __name__ == '__main__':
    try:
        main()
    except:
        print('Main failed.')
else:
    print('Program failed. Please run independently.')