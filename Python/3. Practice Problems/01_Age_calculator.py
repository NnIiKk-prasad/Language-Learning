# Practice Problem 1 - Age calculator

# customisable input
currentYear = 2021

try:
    ageOrYear = int(input("Enter your age or year of birth: "))
    if ageOrYear <= 0:
        print("Invalid Input")
        exit()

    if ageOrYear > 0 and ageOrYear <= 125:
        ageOrYear = currentYear - ageOrYear

    if ageOrYear > 125 and ageOrYear < 1896:
        print("You seems to be oldest person alive")
        exit()

    if ageOrYear > currentYear:
        print("You are not yet born")
        exit()

    if ageOrYear <= currentYear - 100:
        print(f"You have become 100 yrs old in {ageOrYear + 100}")
    else:
        print(f"You'll become 100 yrs old in {ageOrYear + 100}")

    while True:
        print("\nDo you want to check your age at a particular year?")
        ch = input("Press Y or N: ").capitalize()
        if ch == 'Y':
            year = int(input("Type an year: "))
            print(f"Your age in {year} is {year - ageOrYear}")
        elif ch == 'N':
            break
        else:
            print("Invalid Input")
except ValueError:
    print("Enter integers only")
    exit()
