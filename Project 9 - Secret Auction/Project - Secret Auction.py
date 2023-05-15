import Art

print(Art.greeting)
print(Art.logo)

bidders = []


def add_bidder(name, bid):
    # Create a dictionary with the bidder's name as the key and their bid as the value
    bidder = {
        name: bid
    }
    # Append the bidder dictionary to the bidders list
    bidders.append(bidder)


def bid_winner():
    highest_bid = 0
    highest_bidder = ""

    for bidder in bidders:
        for name, bid in bidder.items():
            if bid > highest_bid:
                # Update the highest_bid and highest_bidder variables if a higher bid is found
                highest_bid = bid
                highest_bidder = name

    if highest_bidder != "":
        print("The highest bidder is:", highest_bidder)
        print("The highest bid amount is:", highest_bid)
    else:
        print("No bidders found")


finish_bid = False
while finish_bid is False:

    bidder_name = input("Enter your name.\n")
    bid_amount = int(input("How much would you like to bid?\n"))
    choice = input("Would you like to add a bid? Type 'yes'.\nIf you would like to quit type 'quit'.\n").lower()

    if choice == 'quit':
        # Add the bidder's name and bid to the bidders list and set finish_bid to True to exit the loop
        add_bidder(name=bidder_name, bid=bid_amount)
        finish_bid = True
    elif choice == 'yes':
        # Add the bidder's name and bid to the bidders list
        add_bidder(name=bidder_name, bid=bid_amount)
    else:
        print("You have keyed in an invalid choice.\nTry again\n")
        continue

# Determine the highest bidder and the highest bid amount
bid_winner()
