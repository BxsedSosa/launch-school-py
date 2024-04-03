'''
The following function returns a list of the remainders of dividing the numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []
'''
def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(remainders_3(numbers_1))
print(remainders_3(numbers_2))
print(remainders_3(numbers_3))
print(remainders_3(numbers_4))

'''
It would be list 1 & 2
'''