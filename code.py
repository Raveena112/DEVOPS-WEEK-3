def is_leap_year(year):
    # Check if the year is divisible by 4
    if (year % 4 == 0):
        # If the year is divisible by 100, it must also be divisible by 400
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Get user input
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
