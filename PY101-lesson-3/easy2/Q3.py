"""
Q3. Programmatically determine whether '42' lies between 10 and 100, includsive. Do the same for the values 100 and 101
"""


def find_num(num):

    if num >= 10 and num <= 100:
        return True

    return False


print(find_num(42))
print(find_num(101))
