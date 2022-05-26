'''ASCII Shapes, Problem 2. Written by Cael Shoop.'''
import sys

# Function to print rectanges. Fill is a boolean for whether or not the shape is filled.
def print_rect(height, width, fill):
    for ii in range(height):
        for jj in range(width):
            # Filled rectangles get * everywhere
            if fill:
                sys.stdout.write('*')
            # Non-filled rectangles get specific * placement
            else:
                # Top and bottom rows get *
                if ii == 0 or ii == height - 1:
                    sys.stdout.write('*')
                # Insides get filled with spaces
                elif jj > 0 and jj < width - 1:
                    sys.stdout.write(' ')
                # Edges get *
                else:
                    sys.stdout.write('*')
        sys.stdout.write('\n')
    sys.stdout.write('\n')

# Function to print triangles. Fill is a bool for whether or not it is filled.
def print_tri(height, fill):
    width = height * 2 - 1
    count = 0
    for ii in range(height):
        for jj in range(width):
            # If the triangle is to be filled
            if fill:
                if jj <= count:
                    sys.stdout.write('*')
                else:
                    break
            # If the triangle is to be empty
            else:
                # Compares current height to count.
                if jj <= count:
                    # Checks if current location is not last, first, or bottom.
                    if jj > 0 and jj < count and ii != height - 1:
                        sys.stdout.write(' ')
                    # Alternates bottom line with * and space
                    elif ii == height - 1 and jj % 2 == 1:
                        sys.stdout.write(' ')
                    else:
                        sys.stdout.write('*')
                else:
                    break
        count = count + 2
        sys.stdout.write('\n')
    sys.stdout.write('\n')


def main():
    print('Welcome to ASCII Shapes!')
    # Menu loop
    while True:
        choice = 0
        # Menu selection check
        while choice < 1 or choice > 5:
            print('Please select an option from the menu.')
            print('\t1. Filled rectangle')
            print('\t2. Empty rectangle')
            print('\t3. Filled triangle')
            print('\t4. Empty triangle')
            print('\t5. Quit')
            # Check if input is an integer and within parameters
            try:
                choice = int(input('Selection: '))
                if choice < 1 or choice > 5:
                    print('Please enter a choice between 0 and 5.')
            except:
                print('Please enter an integer.')
        # If quit is chosen, say goodbye and break
        if choice == 5:
            print('Goodbye!')
            break
        # Take shape height info from user
        height = 0
        while height < 1:
            # Check if input is integer and within parameters
            try:
                if choice < 3:
                    height = int(input('Please enter the rectangle\'s height: '))
                else:
                    height = int(input('Please enter the triangle\'s height: '))
                if height < 1:
                    print('Please enter a height larger than 0.')
            except:
                print('Please enter an integer.')
        # Take shape width info from user if shape is rectangle
        if choice == 1 or choice == 2:
            width = 0
            while width < 1:
                # Check if input is integer and within parameters
                try:
                    width = int(input('Please enter the rectangle\'s width: '))
                    if width < 1:
                        print('Please enter a width larger than 0.')
                except:
                    print('Please enter an integer.')
        # Formatting newline
        sys.stdout.write('\n')
        # Call shape print function based on menu selection
        if choice == 1:
            print_rect(height, width, True)
        elif choice == 2:
            print_rect(height, width, False)
        elif choice == 3:
            print_tri(height, True)
        elif choice == 4:
            print_tri(height, False)


if __name__ == '__main__':
    try:
        main()
    except:
        print('Main failed.')
else:
    print('Program failed. Please run independently.')