## Blackjack Game

This program allows you to play a game of Blackjack against the computer. It uses a text-based interface to simulate the game. The rules of Blackjack are as follows:

- The goal of the game is to get as close to 21 as possible without going over.
- Numbered cards (2-10) are worth their face value. Face cards (Jacks, Queens, and Kings) are worth 10.
- An Ace can be worth either 1 or 11, depending on which value is more advantageous.
- The deck is unlimited in size. There are no jokers.
- Each player is dealt two cards initially from a deck of cards.
- Cards in the deck have equal probability of being drawn, and they are not removed from the deck as they are drawn.
- The computer serves as the dealer.

To play the game, run the program and follow the prompts. You will be asked if you want to play a game of Blackjack. Enter 'y' to start a game or 'n' to exit.

During the game, you will see your initial cards and their total score. You can choose to draw another card ('y') or pass ('n'). The program will then update your score and ask for your decision again until you either reach a score of 21, go bust, or choose to pass.

Once you finish your turn, the computer will automatically play its turn. It will draw cards until it reaches a score of at least 17. After that, the final hands and scores of both players will be displayed, and the winner will be determined based on the rules mentioned above.

You will then be asked if you want to play another game of Blackjack. Enter 'y' to start a new game or 'n' to exit the program.

Assumptions:
- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards: `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- The cards in the list have an equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

Have fun playing Blackjack!
