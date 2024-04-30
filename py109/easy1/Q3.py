"""
Q3. Print all even numbers from 1 to 99, inclusive, with each number on a seperate line

Bonus: Can you solve the problem by iterating over just the even numbers?
"""

even_numbers = [i for i in range(2, 100, 2)]

for number in even_numbers:
    print(number)

"""
This code will be just like Q2's answer but the only difference really is the starting number for the range function since we are only using all even numbers then we would start at 2 instead of 1
"""
