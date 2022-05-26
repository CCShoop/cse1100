'''Written by Cael Shoop. Checkerboard pattern for problem 4.'''


def main():
    for ii in range(7):
        # Odd rows get a space at the beginning and are shortened by one
        if ii % 2 == 1:
            # Using 'end=""' to eradicate the automatic newline in print
            print(" ", end="")
            jj = jj + 1
        # Printing out rows
        for jj in range(8):
            print("* ", end="")
        # I could use 'print("")' but this is too cursed not to be used
        print("\n", end="")


if __name__ == '__main__':
    try:
        main()
    except:
        print('Main failed.')
else:
    print('Program failed. Please run independently.')