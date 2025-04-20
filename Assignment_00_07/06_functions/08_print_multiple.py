def print_multiple(message: str, repeats: int):
    """Print the message 'repeats' number of times."""
    for i in range(repeats):  
        print(message)  

def main():
    message = input("Please type a message: ") 

    
    while True:
        try:
            repeats = int(input("Enter a number of times to repeat your message: ")) 
            break  
        except ValueError:
            print("Invalid input! Please enter a valid integer.") 

    print_multiple(message, repeats)  


if __name__ == '__main__':
    main()
