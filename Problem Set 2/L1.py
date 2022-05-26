'''Challenge L1 written by Cael Shoop for Problem Set 2 in CSE1100.'''


def main():
    for count in range(200):
        ii = count + 1  # Because count is 0-199, ii is 1-200
        value = str(ii) # Change iterable to a string
        if ii % 3 == 0 and ii % 5 != 0:   # If multiple of 3 and not 5, print Fizz
            print('Fizz', end='')
        elif ii % 5 == 0 and ii % 3 != 0: # If multiple of 5 and not 3, print Buzz
            print('*Buzz*', end='')
        elif ii % 3 == 0 and ii % 5 == 0: # If multiple of 3 and 5, print Bang
            print('BANG!!', end='')
        else:                             # If not multiple of 3 or 5, print value
            print(value, end='')
        if ii % 10 != 0:                  # If not last value of line, don't print newline
            print(', ', end='')
        else:                             # If last value of line, print newline
            print()


if __name__ == '__main__':
    main()