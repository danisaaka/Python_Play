import random
from game_data import data
from higher_lower_art import logo, vs
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def higher_lower_start():
    score = 0
    end_game = False

    # Select two random dictionaries
    dict_a = random.choice(data)
    dict_b = random.choice(data)

    while not end_game:

        # Make sure dict_b is different from dict_a
        while dict_b == dict_a:
            dict_b = random.choice(data)

        # Present the two dictionaries to the user
        print(f"Compare A: {dict_a['name']}, a {dict_a['description']} from {dict_a['country']}.")
        print(vs)
        print(f"Against B: {dict_b['name']}, a {dict_b['description']} from {dict_b['country']}.")

        # Ask the user to choose which of the two option has a higher follower count
        valid_inputs = ['higher', 'lower']
        user_guess = input("Is B's follower count higher or lower than A? Type 'higher' or 'lower': ").lower()

        # Validate the user's input
        while user_guess not in valid_inputs:
            user_guess = input("Invalid input. Type 'higher' or 'lower':\n ").lower()

        if user_guess == 'higher':
            # Compare the follower counts
            if dict_a['follower_count'] > dict_b['follower_count']:
                score += 1
            else:
                pass
        elif user_guess == 'lower':
            if dict_a['follower_count'] < dict_b['follower_count']:
                score += 1
            else:
                pass
        else:
            pass

        # Compare the follower counts
        if (user_guess == 'higher' and dict_b['follower_count'] > dict_a['follower_count']) or \
                (user_guess == 'lower' and dict_b['follower_count'] < dict_a['follower_count']):
            score += 1
            print(f"You're right!\nYour current score is {score}\n")
        else:
            end_game = True
            print("Oops! That's incorrect. Game over.")

        # Update dict_a for the next round
        dict_a = dict_b
        clear_console()

    print(f"Your final score is: {score}")


game_over = False
while game_over is not True:
    print(logo)
    higher_lower_start()
    play_again = input("Would you like to play again?\nPress y to play again or any other key to quit.").lower()
    if play_again == 'y':
        higher_lower_start()
    else:
        print("Thanks for playing!")
        game_over = True
