"""
7. Write a find_integer functino that returns a list of all the integers from my_tuple:
"""


def find_integers(tup):
    new_list = []
    for element in tup:
        if type(element) is int:
            new_list.append(element)

    return new_list


my_tuple = (1, "a", "1", 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)
