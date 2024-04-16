"""
6. Write a function that checks whether a string is empty or not
"""


def is_empty(string):
    if string == "":
        return True
    else:
        return False


print(is_empty("mars"))
print(is_empty("   "))
print(is_empty(""))
