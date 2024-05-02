"""
Q10. Build a program that displays when the user will retire and how many years they have to work till retirement
"""

CURRENT_YEAR = 2024
age = int(input("What is yoyur age?: "))
retire_age = int(input("At what age would you like to retire?: "))


print(f"It's {CURRENT_YEAR}. You will retire in {CURRENT_YEAR + retire_age}")
print(f"You only have {retire_age - age} years of work to go")
