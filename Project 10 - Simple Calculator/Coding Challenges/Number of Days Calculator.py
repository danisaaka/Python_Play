def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # Leap year
                return True
            else:
                # Not leap year.
                return False
        else:
            # Leap year.
            return True
    else:
        # Not leap year.
        return False


def days_in_month(year, month):
    leap_year = is_leap(year)
    if leap_year is True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(f"The year {year} is a leap year.")
    elif leap_year is False:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(f"The year {year} is not a leap year.")
    month_name = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
    number_of_days = month_days[month - 1]
    name_of_month = month_name[month - 1]
    message = f"Month {month} is {name_of_month} and it has {number_of_days} days"
    return message


# 🚨 Do NOT change any of the code below

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
