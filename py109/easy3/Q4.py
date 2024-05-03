"""
Q4. Write a function that takes one arugmnet, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer
"""


def stringy(number):
    string = []
    for i in range(number):
        if i % 2 == 0:
            string.append("1")
        else:
            string.append("0")

    return "".join(string)


print(stringy(6) == "101010")  # True
print(stringy(9) == "101010101")  # True
print(stringy(4) == "1010")  # True
print(stringy(7) == "1010101")  # True
