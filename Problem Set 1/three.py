'''Written by Cael Shoop. Third problem, identifies palindromes.'''
import math


def is_palindrome(num):
    # Compares first number to fifth number
    if math.floor(num/10000)%10 != num%10:
        return False
    # Compares second number to fourths number
    elif math.floor(num/1000)%10 != math.floor(num/10)%10:
        return False
    return True


def main():
    num = 0
    while num != -1:
        # Checks if input number matches parameters
        while (num < 10000 or num > 99999) and num != -1:
            # Makes sure input is an integer, correct length, and not a quit condition
            try:
                num = int(input('Enter a five-digit integer (or -1 to quit): '))
                if (num < 10000 or num > 99999) and num != -1:
                    print(f'The number {num} is not a five-digit number.\n')
                elif num == -1:
                    break
            except:
                print('Please enter an integer.')
        # If the user is not quitting, check if input is a palindrome
        if num != -1:
            if is_palindrome(num):
                print(f'The number {num} is a palindrome!\n')
            else:
                print(f'The number {num} is not a palindrome.\n')
            # Reset input for next loop. Without this, it will infinitely loop with
            # the given input. Don't ask me how I was reminded of this.
            num = 0
    print('Good bye!')


if __name__ == '__main__':
    try:
        main()
    except:
        print('Main failed.')
else:
    print('Program failed. Please run independently.')