def game_intro():
    """Welcomes the user and lets them choose between hard and easy mode.
    Hard mode = 5 chances. Easy Mode = 10 modes"""
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    user_choice = input("Choose difficulty. Type 'easy' or 'hard\n").lower()
    if user_choice == 'easy':
        return EASY_MODE
    elif user_choice == 'hard':
        return HARD_MODE
    else:
        return "You have selected an invalid option"


def generate_random_number():
    """The program generates a random number that will be guessed by the user"""
    import random
    random_number = random.randint(1, 100)
    return random_number


def play_number_game():
    # These are the values that will be passed on to the game
    NUMBER_TO_GUESS = generate_random_number()
    number_of_chances = game_intro()

    # Ask the user to guess a number until they are out of chances
    while number_of_chances != 0:
        try:
            user_guess = int(input("Choose a number between 1 and 100.\n"))
            if user_guess == NUMBER_TO_GUESS:
                print(f"You are correct!\nThe right answer is {NUMBER_TO_GUESS}\nYou win!")
                break
            elif user_guess > NUMBER_TO_GUESS:
                number_of_chances -= 1
                print(f"Too high. Try again. You have {number_of_chances} chances left")
            elif user_guess < NUMBER_TO_GUESS:
                number_of_chances -= 1
                print(f"Too low. Try again. You have {number_of_chances} chances left")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if number_of_chances == 0:
        print(f"Oops! You are out of chances. The answer was {NUMBER_TO_GUESS} \nTry Again")


# Assigned Global Constants to determine the number of lives to give to user
EASY_MODE = 10
HARD_MODE = 5
start_game = True
# Main loop that will keep the game running until the user decides to quit
while start_game is True:
    from number_guessing_logo import logo
    print(logo)
    start_game_prompt = input("Do you want to play the Number Guessing Game?\nPress 'y' for yes or 'n' for no.\n")
    if start_game_prompt == 'y':
        play_number_game()
    elif start_game_prompt == 'n':
        start_game = False
    else:
        print("You have selected and invalid option. Try again")
