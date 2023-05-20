def leap_year_checker():
    try:
        year = int(input("\nWhich year do you want to check?\n"))
        if year < 0:
            print("You have keyed in a negative year number.")
        else:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("Leap year.")
                    else:
                        print("Not leap year.")
                else:
                    print("Leap year.")
            else:
                print("Not leap year.")

    except ValueError:
        print("You keyed in an incorrect input.")


program_exit = False
while program_exit is not True:
    leap_year_checker()
    keep_looping = input("Press 'n' to quit or any other key to check another year.\n").lower()
    if keep_looping == 'n':
        program_exit = True
