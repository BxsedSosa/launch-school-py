"""
Q11. Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should only return exactly one charcter. if its even 2
"""


def center_of(string):
    string_len = len(string)
    half_len = string_len // 2
    print(half_len)

    if string_len % 2 == 0:
        print(string[half_len - 1 : half_len + 1])
        return string[half_len - 1 : half_len + 1]
    else:
        print(string[half_len - 1])
        return string[half_len - 1]


print(center_of("I Love Python!!!") == "Py")  # True
print(center_of("Launch School") == " ")  # True
print(center_of("Launchschool") == "hs")  # True
print(center_of("Launch") == "un")  # True
print(center_of("Launch School is #1") == "h")  # True
print(center_of("x") == "x")  # True
