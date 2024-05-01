"""
Q10. Write a function that computes the sum of all numbers between `1` and some other number, inclusive, that are multiples of `3 or 5`

For instance, if the supplied number is 20, the result should be 98
"""


def multisum(number):
    total = 0

    for num in range(number + 1):
        if num % 3 == 0 or num % 5 == 0:
            total += num

    return total


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)


"""
in this code we define the functino `multisum`. Creating a variable called total equal to 0 and then starting a for loop with the range of the argument being a integer + 1 so we are being inclusive to the number used as the argument. Then each iteration of num goes through a if statment check if its a multiple of 3 or 5 then adding to the total. Once completed then the total is returned
"""
