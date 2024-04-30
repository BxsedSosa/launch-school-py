"""
Q8. Write a fucntion that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not

For simplicity, this exercise assumes that the Gregorian calendar has been in continouous use since the year 1. We'll address that assumption in the next exercise that follows this one

To determine whether a given year is a leap year, use the rules of Gregorian calendar:

- If the year is divisible by 400, it IS a leap year
- If the year is divisible by 100, but not by 400, it IS NOT a leap year
- If the year is divisible by 4 but not by 100, it IS a leap year
- All other years ARE NOT leap years
"""


def is_leap_year(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0


# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

"""
This one more self explanatory since its just condional expresions and if they evaluate as True then return the True or False
"""
