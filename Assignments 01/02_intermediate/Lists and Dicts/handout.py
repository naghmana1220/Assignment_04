# ---------- Problem 1 ----------
def fruit_list_practice():
    # Create a list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of the list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)


# ---------- Problem 2 ----------
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range!"

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid slicing range!"

def index_game():
    my_list = ['cat', 'dog', 'fish', 'bird', 'lion']
    
    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit to Main Menu")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)
        
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated List:", result)
        
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced List:", result)
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Try again!")


# ---------- Main Menu ----------
def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Run Fruit List Practice (Problem #1)")
        print("2. Play Index Game (Problem #2)")
        print("3. Exit")

        user_choice = input("Choose an option (1-3): ")

        if user_choice == '1':
            fruit_list_practice()
        elif user_choice == '2':
            index_game()
        elif user_choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
