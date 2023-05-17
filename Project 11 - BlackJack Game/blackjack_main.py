import random
import os

# List of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to deal a random card from the cards list
def deal_card():
    random_card = random.choice(cards)
    return random_card


# Function to calculate the score of a list of cards
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Function to compare the scores of the user and computer and determine the outcome
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


# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to play the game of blackjack
def play_blackjack():
    from blackjack_Art import logo
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    # Deal 2 cards to the user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Game loop until the game is over
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display user's cards and current score
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if the game is over based on scores
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display the final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


clear_console()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_console()
    play_blackjack()
