"""
Q5. The following function unnecessarily uses two return  statements to retrun boolean values. Can you rewrite this funtion so it only has one return statement and does not explicitly use either True or False?
"""


def is_color_valid(color):

    return color == "blue" or color == "green"


print(is_color_valid("blue"))
print(is_color_valid("red"))
