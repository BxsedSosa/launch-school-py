"""
6. Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second strng is shorter and 0 if theyre of equal length
"""


def compare_by_length(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    if str1_len < str2_len:
        return -1
    elif str2_len < str1_len:
        return 1
    else:
        return 0


print(compare_by_length("patience", "perseverance"))
print(compare_by_length("strength", "dignity"))
print(compare_by_length("humor", "grace"))
