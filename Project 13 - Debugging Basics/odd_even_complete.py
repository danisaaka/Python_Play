program_exit = False
while not program_exit:
    try:
        number = int(input("Which number do you want to check?\n"))  # Prompt user to input a number
        if number < 0:
            print("Please enter a positive number.")  # Notify the user to enter a positive number
        else:
            if number % 2 == 0:
                print("This is an even number.")  # Display a message if the number is even
            else:
                print("This is an odd number.")  # Display a message if the number is odd

            valid_input = False
            while valid_input is not True:
                user_input = input("Do you want to check another number?\nType 'y' or 'n'.\n").lower()
                if user_input == 'y':
                    valid_input = True  # Set valid_input to True to repeat the while loop for another number
                elif user_input == 'n':
                    valid_input = True
                    program_exit = True  # Set program_exit to True to exit the while loop and terminate the program
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")  # Notify the user of an invalid input
    except ValueError:
        print(
            "You have given incorrect input. Please enter a valid number.")  # Notify the user of an invalid number
        # input
