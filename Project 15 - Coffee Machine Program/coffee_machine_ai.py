from coffee_machine_inputs import MENU, resources

valid_inputs = ["espresso", "latte", "cappuccino", "off", "report"]

total_sales = 0
order_count = 0


def print_report():
    """Prints the report of the current resource levels, total sales, and order count in the machine."""
    print("===== Machine Report =====")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Total Orders: {order_count}")
    print("==========================")


while True:
    prompt = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    if prompt == "off":
        print("Machine turned off.")
        break

    if prompt == "report":
        print_report()
        continue

    if prompt not in valid_inputs:
        print("I'm sorry, I don't understand that.\nPlease choose from the available options")
        continue

    coffee = MENU[prompt]
    ingredients = coffee["ingredients"]

    if any(resources[ingredient] < quantity for ingredient, quantity in ingredients.items()):
        print("Please choose another coffee or refill the machine.")
        continue

    cost = coffee["cost"]
    print(f"The cost of {prompt} is ${cost:.2f}. Proceeding to Payment...")

    try:
        quarters = int(input("How many quarters?\n"))
        dimes = int(input("How many dimes?\n"))
        nickels = int(input("How many nickels?\n"))
        pennies = int(input("How many pennies?\n"))
        if quarters < 0 or dimes < 0 or nickels < 0 or pennies < 0:
            raise ValueError
    except ValueError:
        print("Invalid input for coin count. Please enter a valid non-negative integer amount.")
        continue

    total_paid = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    if total_paid < cost:
        print("Insufficient payment. Refunding amount")
        print(f"Amount refunded: ${total_paid:.2f}")
        continue

    for ingredient, quantity in ingredients.items():
        resources[ingredient] -= quantity

    resources["money"] += cost
    total_sales += cost
    order_count += 1

    change = total_paid - cost
    if change > 0:
        resources["money"] -= change
        print(f"Enjoy your {prompt}! Here is your change: ${change:.2f}")
    else:
        print(f"Enjoy your {prompt}!")

print_report()
