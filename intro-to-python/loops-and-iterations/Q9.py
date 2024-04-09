"""
9. Write a function that computes and returns the factorial of a number by using a for or while loop. the factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n inslusive.
"""


def factorial(number):
    result = 1

    for num in range(1, number + 1):
        result = result * num

    return result


print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
