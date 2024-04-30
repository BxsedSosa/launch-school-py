"""
Q2. Alan wrote the following function, which was intended to return all of the factors of `number`

Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looing to find the factors of negative numbers, but we want to handle it gracefully instead of going into an infinite loop

Bonus Q: What is the purpose of `number % divisor == 0` in that code?
"""


def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result


print(factors(15))

"""
This `number % divisor == 0`

is seeing if the number is divisiable to the divisor with no remainder
"""
