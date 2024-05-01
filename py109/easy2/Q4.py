"""
Q4. Using the multply function from the "Multiplying Two numbers" exercise, write a function that computes the square of its arugment (the square is the result of multiplying a number by itself)
"""


def multiply(number1, number2):
    return number1 * number2


def square(number):
    return multiply(number, number)


print(square(5) == 25)  # True
print(square(-8) == 64)  # True
