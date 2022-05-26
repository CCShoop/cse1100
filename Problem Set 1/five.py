'''Written by Cael Shoop. Problem 5, Connectivity Calculator.'''


def main():
    num = 0
    # Loop to check input
    while num < 1:
        # Makes sure input is a positive integer
        try:
            num = int(input('Enter an integer n: '))
            if num < 1:
                print('Please enter a positive value for n.')
            else:
                break
        except:
            print('Please enter an integer.')
    # Safely counts the number of connections using a choose 2 formula
    try:
        conns = int((num * (num - 1)) / 2)
        # Corrected output
        if conns == 0:
            print(f'n={num} has no possible point-to-point connections.')
        elif conns == 1:
            print(f'n={num} has K{num}=1 possible point-to-point connection.')
        else:
            print(f'n={num} has K{num}={conns} possible point-to-point connections.')
    except:
        print('Connection formula failed.')


if __name__ == '__main__':
    try:
        main()
    except:
        print('Main failed.')
else:
    print('Program failed. Please run independently.')