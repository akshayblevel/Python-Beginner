def printvalue():
    # ~ compliment
    x = 14
    # Binary of 14 is 00001110
    # Compliment of above number is reverse of binary number that is 11110001
    print(~x)  # -15
    # How come -15?
    # Binary of 15 is 00001111
    # Now 1s compliment of above number is 11110000
    # Add 1 in above number to get 2s compliment that is 11110001 which equals -15



if __name__ == '__main__':
    printvalue()
