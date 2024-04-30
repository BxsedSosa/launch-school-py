"""
Q1. Write a function that takes one integer argument and returns `True` when the number's absolute value is odd, `False` otherwise
"""


def is_even(number):
    if abs(number) % 2 == 0:
        return True
    else:
        return False


print(is_even(2))
print(is_even(3))
print(is_even(5))
print(is_even(-6))
print(is_even(0))
print(is_even(9))
print(is_even(-12))

"""
The question asked us to create a function that will determine if a number thats inputted will return True if its even and False for odd but also making sure you are getting the absolute number. 

Absolute number is when you have a negative number and you automatically change it to positive
"""
