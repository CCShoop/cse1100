'''Lab 1 Problem 2 program written by Cael Shoop for CSE1100.'''


def main():
    # Takes user's name as input in 'name'
    name = input('Hello! What is your name?\n')
    # Takes user's favorite food and stores it as input in 'food'
    food = input('What is your favorite food?\n')
    # Combines script with entered information during print statement
    print('Great to meet you, ' + name + '! ' + food + ' sounds tasty!')

    #print('Great to meet you, ' + input('Hello! What is your name?\n') +
    #      '! ' + input('What is your favorite food?\n') + ' sounds tasty!')


if __name__ == '__main__':
    main()
