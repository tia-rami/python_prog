# Write your solution here
from datetime import datetime

def calculate_age(day: int, month: int, year: int):
    user_age = datetime(year, month, day)
    new_millenium_eve = datetime(1999, 12, 31)

    difference = new_millenium_eve - user_age
    return difference.days

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
age = calculate_age(day, month, year)

if (age < 0):
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {age} days old on the eve of the new millennium.")
