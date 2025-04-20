def main():
    for i in range(10, 20):  # Loop through numbers from 10 to 19
        if is_odd(i):
            print(f'{i} odd')  # Print the number and 'odd' if it's odd
        else:
            print(f'{i} even')  # Print the number and 'even' if it's even

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  
    return remainder == 1  


if __name__ == '__main__':
    main()  
