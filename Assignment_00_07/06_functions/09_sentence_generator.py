def make_sentence(word, part_of_speech):
    """Generates and prints a sentence based on the part of speech."""
    if part_of_speech == 0:
       
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
      
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
      
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def get_valid_part_of_speech():
    """Helper function to ensure the user provides a valid part of speech number (0, 1, or 2)."""
    while True:
        user_input = input("Type 0 for noun, 1 for verb, 2 for adjective: ")
        if user_input.isdigit() and int(user_input) in [0, 1, 2]:
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid number: 0, 1, or 2.")

def main():
    
    word = input("Please type a noun, verb, or adjective: ")
    
   
    part_of_speech = get_valid_part_of_speech()

    
    make_sentence(word, part_of_speech)


if __name__ == '__main__':
    main()

