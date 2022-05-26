'''Written by Cael Shoop. CSE1100 Lab 2 Problem 2.'''

from math import *


def main():
    # Input
    num0, num1, num2 = input('Please enter three different numbers\n').split(' ')

    # Conversions
    nums = []
    nums.append(float(num0))
    nums.append(float(num1))
    nums.append(float(num2))
    avg = sum(nums) / len(nums)

    # Output
    print('Thanks. Here are the results:')
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
