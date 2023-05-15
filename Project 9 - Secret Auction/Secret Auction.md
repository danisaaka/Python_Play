# Secret Auction Program

This program allows bidders to participate in a silent auction and determines the highest bidder and the highest bid amount at the end.

## Program Explanation

The program consists of the following components:

1. The `bidders` list: This list stores the bidder information.

2. The `add_bidder()` function: This function adds a new bidder to the `bidders` list. It takes the bidder's name and bid amount as arguments, creates a dictionary with the bidder's name as the key and their bid amount as the value, and appends the dictionary to the `bidders` list.

3. The `bid_winner()` function: This function determines the highest bidder and the highest bid amount from the `bidders` list. It initializes `highest_bid` and `highest_bidder` variables to keep track of the highest bid amount and bidder. The function loops through each bidder in the `bidders` list and compares their bid amount with the current highest bid. If a higher bid is found, the `highest_bid` and `highest_bidder` variables are updated.

4. The bidding process: The program uses a `while` loop to allow users to enter their name and bid amount. The loop continues until the user decides to quit. The user is prompted to enter their name, bid amount, and a choice to add another bid or quit the program. If the user chooses to quit, their name and bid amount are added to the `bidders` list using the `add_bidder()` function, and the loop is exited. If the user chooses to add another bid, their name and bid amount are added to the `bidders` list.

5. Displaying the result: After the bidding process is completed, the `bid_winner()` function is called to determine the highest bidder and bid amount. The program then displays the highest bidder's name and the corresponding bid amount.

## Usage

To use the program, follow these steps:

1. Run the program in a Python environment.

2. Enter the bidder's name when prompted.

3. Enter the bid amount when prompted.

4. Choose to add another bid or quit the program by typing 'yes' or 'quit' respectively.

5. Repeat steps 2-4 to enter bids from multiple bidders.

6. Once all bids are entered, the program will display the highest bidder and their bid amount.

## Error Handling

The program includes basic error handling. If the user enters an invalid choice during the bidding process, an error message is displayed, and they are prompted to try again.

Please note that this explanation provides a high-level overview of the program's functionality. For detailed implementation and code, refer to the program's source code.

