## Number Guessing Game

This program allows the user to play a number guessing game. The computer generates a random number between 1 and 100, and the user needs to guess the correct number within a certain number of chances. The game offers two difficulty modes: easy and hard.

### Function: game_intro

This function welcomes the user and lets them choose between the easy and hard difficulty modes. It prompts the user to enter their choice and returns the corresponding number of chances for the chosen difficulty mode.

#### Parameters

None

#### Returns

- `EASY_MODE` (constant) if the user chooses the easy difficulty mode.
- `HARD_MODE` (constant) if the user chooses the hard difficulty mode.
- `"You have selected an invalid option"` if the user enters an invalid choice.

### Function: generate_random_number

This function generates a random number between 1 and 100, which will be the number the user needs to guess.

#### Parameters

None

#### Returns

A randomly generated number between 1 and 100.

### Function: play_number_game

This function runs the main number guessing game. It generates a random number using `generate_random_number()` and retrieves the number of chances using `game_intro()`. The user is prompted to guess a number, and the program provides feedback based on the guess.

#### Parameters

None

#### Returns

None

### Error Handling

The program uses a `try-except` block to handle potential `ValueError` exceptions that may occur when the user enters an invalid guess. If the input cannot be converted to an integer, an error message is displayed, and the user can continue guessing.

### Global Constants

- `EASY_MODE`: Represents the number of chances given in the easy difficulty mode.
- `HARD_MODE`: Represents the number of chances given in the hard difficulty mode.

### Main Loop

The main loop keeps the game running until the user decides to quit. It displays a game logo, prompts the user to start the game, and calls the `play_number_game()` function accordingly. If the user selects an invalid option, an error message is displayed.

