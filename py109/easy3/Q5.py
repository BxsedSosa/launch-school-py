"""
Q5. Write a function that takes a positive integer, n, as an arugment and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle should have one end at the lower-left of the triangle, and the other end at hte upper-right
"""


def triangle(number):

    for i in range(1, number + 1):
        print(f"{" " * (number - i)}{'*' * i}")


triangle(5)
triangle(9)
