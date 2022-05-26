'''Written by Cael Shoop. Lab 3, Problem 1.'''

import random


def main():
    print('Welcome to Guessing Game!')
    print('Please guess a number from 1 to 500:')
    guess = 0
    guesses = 5
    value = random.randrange(1, 500)
    while (guess != value and guesses > 0):
        guess = int(input())
        guesses = guesses - 1
        if (guess < value) and (guesses > 1):
            print(f"That's too low! Try again ({guesses} guesses left).")
        elif (guess > value) and (guesses > 1):
            print(f"That's too high! Try again ({guesses} guesses left).")
        elif (guess < value) and (guesses > 0):
            print(f"That's too low! Last chance ({guesses} guesses left).")
        elif (guess > value) and (guesses > 0):
            print(f"That's too high! Last chance ({guesses} guesses left).")
        elif (guess < value):
            print("That's too low! Better luck next time.")
        elif (guess > value):
            print("That's too high! Better luck next time.")
        else:
            print('You got it! Good job.')
    


if __name__ == '__main__':
    try:
        main()
    except:
        print('Error: Main failed.')
else:
    print('Please run this program independently.')