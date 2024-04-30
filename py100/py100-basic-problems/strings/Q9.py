"""
9. Write a function that checks whether a string startts with a specific prefix
"""

"""
Create a function that takes 2 arguemnts
    a string
    and a prefix that is checking if the string starts with those charcters

we need to get the length of the prefix to be able to get the substring of the string we are checking has those characters

then we will create a if statement checking if the string of the index stopping at the length of the prefix is equal to the prefix then return True

otherwise False
"""


def starts_with(string, prefix):
    len_prefix = len(prefix)
    if string[:len_prefix] == prefix:
        return True
    else:
        return False


print(starts_with("launch", "la"))  # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
