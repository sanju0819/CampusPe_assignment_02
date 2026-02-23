#question number 4
# age calculator
# this program calculates your age in different ways
from datetime import datetime
try:
    birth_year = int(input("enter your birth year: "))
    current_year = datetime.now().year
    my_age = current_year - birth_year

    print("your age:", my_age)
    print("age in months:", my_age * 12)
    print("age in days:", my_age * 365)
    print("age in hours:", my_age * 365 * 24)
    print("age in minutes:", my_age * 365 * 24 * 60)
    print("years left to reach 100:", 100 - my_age)

except:
    print("please enter a valid year")

# bonus part - using exact birth date
print("\n-- bonus: exact age using full birth date --")

try:
    day = int(input("enter birth day: "))
    month = int(input("enter birth month: "))
    year = int(input("enter birth year: "))

    birth_date = datetime(year, month, day)
    today = datetime.now()

    exact_age = today.year - birth_date.year
    # check if birthday has passed this year or not
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        exact_age -= 1

    total_days = (today - birth_date).days

    print("exact age:", exact_age, "years")
    print("total days lived:", total_days)
    print("total months (approx):", exact_age * 12)
    print("total hours (approx):", total_days * 24)
    print("total minutes (approx):", total_days * 24 * 60)
    print("years left to reach 100:", 100 - exact_age)

except:
    print("invalid date entered")