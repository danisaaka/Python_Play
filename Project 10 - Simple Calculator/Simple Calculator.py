from Art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary containing the operation symbols as keys and corresponding functions as values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Function to run the calculator
def calculator():
    print(logo)  # Import Calculator logo from Art.py

    num1 = float(input("What's the first number?: "))

    # Print available operation symbols
    for symbol in operations:
        print(symbol)

    should_continue = True

    # Main calculator loop
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # Select the corresponding calculation function based on the operation symbol
        calculation_function = operations[operation_symbol]

        # Perform the calculation
        answer = calculation_function(num1, num2)

        # Display the result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask the user if they want to continue with the current result or start a new calculation
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            # If the user wants to start a new calculation, recursively call the calculator function
            should_continue = False
            calculator()


calculator()
