'''Written by Cael Shoop. CSE1100 Lab 2 Problem 1.'''

from math import floor


def main():
    # Input
    firstName, lastName = input('Hello! What is your full name?\n').split(' ')
    height = int(input('What is your height (in inches)?\n'))

    # Conversions
    heightFeet = floor(height / 12)
    heightInches = height % 12

    # Output
    print('Great to meet you, ' + firstName + '! Here is your profile:\n')
    print('\tFIRST NAME: ' + firstName)
    print('\tLAST NAME: ' + lastName)
    print('\tHEIGHT: ' + str(heightFeet) + '\' ' + str(heightInches) + '\"\n')


if __name__ == '__main__':
    try:
        main()
    except:
        print('Error. Main failed to execute correctly.')
else:
    print('Please run this script directly.')
