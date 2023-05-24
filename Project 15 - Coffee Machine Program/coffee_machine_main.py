from coffee_machine_inputs import MENU, resources

valid_inputs = ["espresso", "latte", "cappuccino", "off", "report"]


def process_coffee_order(resources):
    """Takes user input for the type of coffee they want, checks if it's a valid input,
    and deducts the required resources from the 'resources' dictionary.

    Args:
        resources (dict): Dictionary representing the available resources in the coffee machine.

    Returns:
        None
    """

    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino)\n").lower()

        if prompt == "off":
            print("Machine turned off.")
            break

        if prompt == "report":
            # Print the current resource levels in the machine
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']:.2f}")
            continue

        if prompt not in valid_inputs:
            print("I'm sorry, I don't understand that.\nPlease choose from the available options")
            continue

        coffee = MENU[prompt]
        ingredients = coffee["ingredients"]

        for ingredient, quantity in ingredients.items():
            if resources[ingredient] < quantity:
                # Check if there are enough resources to make the selected coffee
                print(f"I'm sorry, I don't have enough {ingredient}."
                      f"Please choose another coffee or refill the machine.")
                break
            else:
                cost = coffee["cost"]
                print(f"The cost of {prompt} is ${cost:.2f}\n"
                      f"Proceeding to Payment"
                      f"...")

            # Process coins for payment
            try:
                quarters = int(input("How many quarters?\n"))
                dimes = int(input("How many dimes?\n"))
                nickels = int(input("How many nickels?\n"))
                pennies = int(input("How many pennies?\n"))
            except ValueError:
                print("Invalid input for coin count. Please enter a valid input.")
                break

            total_paid = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

            if total_paid < cost:
                # If the payment is insufficient, refund the amount and break the loop
                print("Insufficient payment. Refunding amount")
                print(f"Amount refunded: ${total_paid:.2f}")
                break

            if total_paid >= cost:
                change = total_paid - cost
                resources["money"] += cost

                for ingredient, quantity in ingredients.items():
                    # Deduct the required ingredients from the resources
                    resources[ingredient] -= quantity

                if change > 0:
                    # If there is change, subtract it from the machine's money and provide the change to the user
                    resources["money"] -= change
                    print(f"Enjoy your {prompt}! Here is your change: ${change:.2f}")
                else:
                    print(f"Enjoy your {prompt}!")


# Run the coffee order processing function
process_coffee_order(resources)
