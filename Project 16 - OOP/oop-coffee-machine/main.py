from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate the MoneyMachine, CoffeeMaker, and Menu classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Variable to control the main loop
is_on = True

# Main loop
while is_on:
    # Get the available menu items
    options = menu.get_items()

    # Prompt the user for their choice
    choice = input(f"What would you like? ({options}):\n")

    if choice == "off":
        # Turn off the coffee machine
        is_on = False
    elif choice == "report":
        # Print the current resources and money status
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the selected drink from the menu
        drink = menu.find_drink(choice)

        if drink is not None:
            # Check if there are enough resources for the selected drink
            if coffee_maker.is_resource_sufficient(drink):
                # Process the payment for the drink
                if money_machine.make_payment(drink.cost):
                    # Make the coffee
                    coffee_maker.make_coffee(drink)
                else:
                    # Insufficient payment, retry or select another drink
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                # Insufficient resources for the drink, notify the user
                print("Sorry, there is not enough resources to make that drink.")
        else:
            # Invalid drink choice, notify the user
            print("Invalid drink selection. Please try again.")

# End of program
