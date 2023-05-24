# Coffee Machine

The coffee machine is a program that allows users to order various types of coffee. It keeps track of available resources and processes payments to provide the selected coffee.

## Usage

To use the coffee machine, follow these steps:

1. Run the program.
2. When prompted, enter the type of coffee you want: espresso, latte, or cappuccino.
3. If you want to turn off the machine, enter "off".
4. To view a report of the current resource levels, enter "report".
5. Follow the instructions to insert coins for payment.
6. If the payment is sufficient, the machine prepares the coffee and provides it to the user.
7. If the payment is insufficient, the machine refunds the amount.
8. Enjoy your coffee!

## Resources

The coffee machine keeps track of the following resources:

- Water: Represents the amount of water available in milliliters (ml).
- Milk: Represents the amount of milk available in milliliters (ml).
- Coffee: Represents the amount of coffee available in grams (g).
- Money: Represents the total amount of money collected by the machine.

## Menu

The coffee machine offers the following types of coffee:

- Espresso: A strong, concentrated coffee made with 50ml of water and 18g of coffee. It costs $1.50.
- Latte: A creamy coffee made with 200ml of water, 150ml of milk, and 24g of coffee. It costs $2.50.
- Cappuccino: A frothy coffee made with 250ml of water, 100ml of milk, and 24g of coffee. It costs $3.00.

## Function Explanation

### `process_coffee_order(resources)`

This function handles the processing of coffee orders. It takes the `resources` dictionary as input, which represents the available resources in the coffee machine.

1. The function runs in a loop, continuously prompting the user for their coffee order until the machine is turned off.
2. If the user enters "off", the function prints a message indicating that the machine has been turned off and breaks the loop.
3. If the user enters "report", the function prints a report of the current resource levels in the machine.
4. If the user enters an invalid input, the function prompts them to choose from the available options and continues the loop.
5. If the user selects a valid coffee option, the function checks if there are sufficient resources to make the coffee. If not, it informs the user and breaks the loop.
6. If there are sufficient resources, the function calculates the cost of the coffee and prompts the user to insert coins for payment.
7. If the payment is insufficient, the function refunds the amount and breaks the loop.
8. If the payment is sufficient, the function deducts the required resources, adds the payment to the machine's money, and provides the coffee to the user.
9. If there is any change, it subtracts the change from the machine's money and provides it to the user.

## Conclusion

The coffee machine program allows users to order different types of coffee, keeps track of available resources, and processes payments. It provides a convenient way to enjoy a cup of coffee while managing resources and finances effectively.
