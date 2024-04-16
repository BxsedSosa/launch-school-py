"""
7. Write a is_empty_or_blank function to determin whether a string is either empty or consists entirely of space
"""


def is_empty_or_blank(string):
    if string == "":
        return True
    elif string == " " * len(string):
        return True
    else:
        return False


print(is_empty_or_blank("mars"))
print(is_empty_or_blank("   "))
print(is_empty_or_blank(""))
