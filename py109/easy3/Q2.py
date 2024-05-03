"""
Q2. Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate charcters collapsed into a single character
"""


def crunch(string):
    current_unique_char = ""
    new_string = []

    for i in range(len(string)):
        if string[i] != current_unique_char:
            current_unique_char = string[i]
            new_string.append(current_unique_char)

    return "".join(new_string)


# These examples should all print True
print(crunch("ddaaiillyy ddoouubbllee") == "daily double")
print(crunch("4444abcabccba") == "4abcabcba")
print(crunch("ggggggggggggggg") == "g")
print(crunch("abc") == "abc")
print(crunch("a") == "a")
print(crunch("") == "")
