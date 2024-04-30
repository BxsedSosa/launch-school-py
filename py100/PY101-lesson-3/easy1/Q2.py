"""
Q2. How can you determine whether a given string ends with an exclamntion mark "!"? Write some code that prints `True` or `False` depending on whether the string ends with an exclamtion mark
"""

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False


def exclamntion_check(string):

    if string[-1] == "!":
        return True
    else:
        return False


print(exclamntion_check(str1))
print(exclamntion_check(str2))
