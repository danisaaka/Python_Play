# Higher Lower Game

This program is a simple game where the user compares the number of Instagram followers between two randomly selected dictionaries. The goal is to guess whether the follower count of the second dictionary is higher or lower than the first.

## How the Game Works

1. The program imports necessary modules, including `random` for generating random values, and uses external data from `game_data.py` and `higher_lower_art.py` for game data and ASCII art, respectively.

2. The `clear_console()` function is defined to clear the console screen.

3. The `higher_lower_start()` function is defined to run the game logic.

4. Inside the `higher_lower_start()` function, the score and end game status are initialized.

5. Two random dictionaries, `dict_a` and `dict_b`, are selected from the provided data.

6. The game loop begins, allowing the user to make guesses.

   - The dictionaries are presented to the user.
   
   - The user is prompted to guess whether the follower count of `dict_b` is higher or lower than `dict_a`.
   
   - The user's input is validated to ensure it is either "higher" or "lower". Error handling is implemented to capture invalid inputs and prompt the user again until a valid input is provided.
   
   - If the guess is correct, the score is incremented and the user is notified.
   
   - If the guess is incorrect, the game ends.
   
   - The `dict_b` becomes the new `dict_a` for the next round.
   
   - The console is cleared for a clean display.
   
7. After the game loop ends, the final score is displayed.

8. The main loop allows the user to play the game multiple times or quit.

   - The logo is displayed.
   
   - The `higher_lower_start()` function is called.
   
   - The user is prompted to play again or quit. Error handling is implemented to capture invalid inputs and end the game if the user does not want to play again.
   
   - If the user chooses to play again, the game restarts.
   
   - If the user chooses to quit, a goodbye message is displayed.

## Error Handling Techniques

1. Input Validation:
   - The user's input for guessing "higher" or "lower" is validated using a while loop and a list of valid inputs. The user is prompted again until a valid input is provided.

2. Invalid Input Handling:
   - If the user enters an invalid input when prompted to play again, an error message is displayed, and the game ends.

Enjoy playing the Higher Lower Game!
