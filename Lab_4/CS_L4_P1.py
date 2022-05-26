'''Written by Cael Shoop. CSE1100 Lab 4 Problem 1, originally Lab 2 Problem 1.'''

from math import floor
import glob
import os


class profile():
    # Create user profile
    def __init__(self, firstName, lastName, height):
        self.firstName = firstName
        self.lastName = lastName
        self.height = height
    # Display user profile
    def show(self):
        print('\tFIRST NAME: ' + self.firstName)
        print('\tLAST NAME: ' + self.lastName)
        print('\tHEIGHT: ' + self.height)
    # Save user profile
    def save(self):
        success = False
        while not success:
            try: # If there is a syntax error, the program will not crash.
                action = input('Would you like to save this profile? (Y/N)\n')
                if action == 'Y' or action == 'y':
                    print('Saving profile...')
                    filename = 'profiles/' + self.firstName + self.lastName + '.txt'
                    file = open(filename, 'w')
                    try: # Writes to the file
                        file.write(self.firstName + '\n' + self.lastName + '\n' + self.height)
                        file.close()
                        print('Profile saved!\n')
                        success = True
                    except:
                        print('Failed to write to file.\n')
                elif action == 'N' or action == 'n':
                    print('Profile will not be saved.\n')
                    success = True
                else:
                    print('Please enter \'Y\' or \'N\'.')
            except:
                print('Please enter \'Y\' or \'N\'.')

# Show all profiles
def show_profiles():
    print('\nHere are the current stored profiles:\n')
    path = 'profiles/' # Reads all .txt files within profiles folder
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            firstName = f.readline().strip('\n') # Reads each line as each variable
            lastName = f.readline().strip('\n')
            height = f.readline().strip('\n')
            current = profile(firstName, lastName, height)
            current.show()
    print('')

# Convert raw height in inches to feet and inches
def convert(height):
    heightFeet = floor(height / 12)
    heightInches = height % 12
    heightstr = str(heightFeet) + '\' ' + str(heightInches) + '"\n'
    return heightstr # Returns the formatted height string

# Reads in user info with checks
def takeInfo():
    success = False
    while (not success):
        try: # First and last name input checking
            firstName, lastName = input('Hello! What is your full name?\n').split(' ')
            if not firstName or not lastName:
                print('Please enter your first and last name with a space in between.')
            else:
                success = True
        except:
            print('Please enter your first and last name with a space in between.')
    success = False
    while (not success):
        try: # Height input checking
            height = int(input('What is your height (in inches)?\n'))
            if not height:
                print('Please enter your height in numerical form, in inches.')
            else:
                success = True
        except:
            print('Please enter your height in numerical form, in inches.')
    return (firstName, lastName, height)

# Displays the main menu and returns a checked input selection
def menu():
    print('(Main Menu) Please select an action:')
    print('\t(1) Enter & Save Data')
    print('\t(2) Load & Show Data')
    print('\t(3) Quit')
    success = False
    while (not success):
        try:
            action = int(input())
            if not action or action < 1 or action > 3:
                print('Please enter a valid menu selection number.')
            else:
                success = True
        except:
            print('Please enter a valid menu selection number.')
    return action


def main():
    repeat = True
    while (repeat):
        choice = menu()
        if choice == 1: # Input & optionally save data
            firstName, lastName, heightraw = takeInfo()
            height = convert(heightraw)
            current = profile(firstName, lastName, height)
            print('Great to meet you, ' + current.firstName + '! Here is your profile:\n')
            current.show()
            current.save()
        elif choice == 2: # Display all saved profiles
            show_profiles()
        else: # Quit
            repeat = False


if __name__ == '__main__':
    try:
        main()
    except:
        print('Error. Main failed to execute correctly.')
else:
    print('Please run this script directly.')
