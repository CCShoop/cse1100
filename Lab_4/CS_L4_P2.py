'''Written by Cael Shoop. CSE1100 Lab 4 Problem 2, originally Lab 2 Problem 2.'''

from math import *

# Runs input checks to ensure all input is valid,
# then returns a list of the inputs as float values.
def secure_input():
    success = False
    while not success:
        try: # Input checking
            num0, num1, num2 = input('Please enter three different numbers\n').split(' ')
            if not num0 or not num1 or not num2:
                print('Please enter three numbers separated by spaces. e.g. \'3 8 7\'')
            else:
                try:
                    nums = []
                    nums.append(float(num0))
                    nums.append(float(num1))
                    nums.append(float(num2))
                    success = True
                    return nums
                except:
                    print('Please enter three numbers separated by spaces. e.g. \'3 8 7\'')
        except:
            print('Please enter three numbers separated by spaces. e.g. \'3 8 7\'')


def main():
    # Input and conversion to list
    nums = secure_input()

    # Calculate average
    avg = sum(nums) / len(nums)

    # Output
    print('\nThanks. Here are the results:')
    print('\tMIN: ' + str(min(nums)))
    print('\tMAX: ' + str(max(nums)))
    print('\tAVG: ' + str(avg) + '\n')


if __name__ == '__main__':
    try:
        main()
    except:
        print('Error. Main failed to execute correctly.')
else:
    print('Please run this script directly.')
