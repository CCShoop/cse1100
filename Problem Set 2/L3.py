'''Challenge L3 written by Cael Shoop for Problem Set 2 in CSE1100.'''

import math
import operator


def main():
    while True:
        # Creates a list out of the input separated by spaces
        expression = input('Enter an Expression (enter \'Q\' to quit): ').split(' ')
        if expression == 'Q' or expression == 'q':
            exit()
        values = [] # List of values that will be used during operations as well
        ops = {'+':operator.add, # Predefined operators from operator library
            '-':operator.sub,    # This tuple allows for easy calling later on
            '*':operator.mul,
            '/':operator.floordiv}
        for char in expression: # Iterates through the expression list
            if char.isnumeric(): # Numbers are inserted into the values list
                values.insert(0, char)
            else:
                if len(values) < 2: # Throws an error if operands do not match up with operators
                    print('Error: Not enough operands in expression.')
                    exit()
                else:
                    if len(char) == 1: # Does the specified operation on the specified operands
                        op0 = float(values.pop(1))
                        op1 = float(values.pop(0))
                        ans = ops[char](op0, op1)
                        values.insert(0, str(ans))
                    else: # Uses math.radians on specified operand
                        op0 = float(values.pop(0))
                        ans = ops[char](math.radians(op0))
                        values.insert(0, str(ans))
        ans = int(ans) # Convert the answer to an integer
        print(f'Result: {ans}')


if __name__ == '__main__':
    main()