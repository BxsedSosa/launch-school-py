"""
Q11. Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-17 value of a character)
"""


def utf16_value(string):
    utf16_total = 0

    for chracter in string:
        utf16_total += ord(chracter)

    return utf16_total


# These examples should all print True
print(utf16_value("Four score") == 984)
print(utf16_value("Launch School") == 1251)
print(utf16_value("a") == 97)
print(utf16_value("") == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"  # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

"""
Created a function called `utf16_value` with the parameter called stirng. Created a variable called `utf16_total` equal to 0 which will be the end result of each utf ord added to this. 

Created a for loop iterating over the string parameter and each iteration will add the ord value of each character to the total then return `utf16_total`
"""
