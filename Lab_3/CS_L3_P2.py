'''Written by Cael Shoop. Lab 3, Problem 2.'''

import math


def main():
    print('Welcome to Converter.')
    choice = 0
    while (choice != 5):
        invalid = 1
        print('Please select from the following conversions:')
        print('\t(1) Kelvin to Fahrenheit')
        print('\t(2) Fahrenheit to Kelvin')
        print('\t(3) Yards to Meters')
        print('\t(4) Meters to Yards')
        print('\t(5) Quit')
        while (invalid == 1):
            try:
                choice = int(input('Enter a selection number: '))
                if (choice < 1 or choice > 5):
                    print('Sorry, that is not a valid choice!')
                    invalid = 1
                else:
                    invalid = 0
            except:
                print('Sorry, that is not a valid choice!')
                invalid = 1
        if (invalid == 0):
            if (choice == 1):
                kelvin = float(input('OK - Kelvin to Fahrenheit. Enter a temperature in Kelvin: '))
                celsius = kelvin - 273.15
                fahrenheit = celsius * (9/5) + 32
                fahrenheit = round(fahrenheit, 4)
                print(f'Thanks. {kelvin} Kelvin is {fahrenheit} Fahrenheit.')
            elif (choice == 2):
                fahrenheit = float(input('OK - Fahrenheit to Kelvin. Enter a temperature in Fahrenheit: '))
                celsius = (fahrenheit - 32) * (5/9)
                kelvin = celsius + 273.15
                kelvin = round(kelvin, 4)
                print(f'Thanks. {fahrenheit} Fahrenheit is {kelvin} Kelvin.')
            elif (choice == 3):
                yards = float(input('OK - Yards to Meters. Enter a distance in yards: '))
                meters = yards * 0.9144
                meters = round(meters, 4)
                print(f'Thanks. {yards} Yards is {meters} Meters.')
            elif (choice == 4):
                meters = float(input('OK - Meters to Yards. Enter a distance in meters: '))
                yards = meters / 0.9144
                yards = round(yards, 4)
                print(f'Thanks. {meters} Meters is {yards} Yards.')
            else:
                print('Thanks for using Converter. Goodbye.')


if __name__ == '__main__':
    try:
        main()
    except:
        print('Error: Main failed.')
else:
    print('Please run this program independently.')