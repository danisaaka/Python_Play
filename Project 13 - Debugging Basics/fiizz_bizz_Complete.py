def fizz_buzz():
    try:
        function_range = int(input("What range do you want the program to run to? Key in a number.\n"))
        for number in range(1, function_range + 1):
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)
    except ValueError:
        print("You keyed in invalid input. Try again")


program_exit = False
while program_exit is not True:
    fizz_buzz()
    keep_looping = input("Press 'n' to quit or any other key to try again.\n").lower()
    if keep_looping == 'n':
        program_exit = True
