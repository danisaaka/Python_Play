import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer wins with a blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"


def play_blackjack():
    clear_console()

    # Deal the user and computer 2 cards each using deal_card() and append().
    user_hand = []
    computer_hand = []

    for _ in range(2):
        user_draw = deal_card()
        user_hand.append(user_draw)

    for _ in range(2):
        computer_draw = deal_card()
        computer_hand.append(computer_draw)

    game_over = False
    while not game_over:
        # Call calculate_score()
        computer_score, user_score = calculate_score(user_hand, computer_hand)

        print(f"Computer's score: {computer_score}")
        print(f"User's score: {user_score}")

        # Hint 9: If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask the user if they want to draw another card.
            user_choice = input("Do you want to draw another card? Type 'y' or 'n': ")
            if user_choice == 'y':
                # Use the deal_card() function to add another card to the user_hand list.
                user_draw = deal_card()
                user_hand.append(user_draw)
            else:
                game_over = True

    # Recheck the score and repeat the checks from Hint 9
    computer_score, user_score = calculate_score(user_hand, computer_hand)

    # Print the final scores
    print(f"Final computer's score: {computer_score}")
    print(f"Final user's score: {user_score}")

    # Compare the scores and determine the winner
    result = compare(user_score, computer_score)
    print(result)

    # Ask the user if they want to restart the game
    restart_choice = input("Do you want to play again? Type 'y' or 'n': ")
    if restart_choice == 'y':
        clear_console()
        play_blackjack()


# Start the game
play_blackjack()
