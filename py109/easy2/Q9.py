"""
Q9. Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number betwen 20 and 100, inclusive
"""

from random import randint

random_num = randint(20, 101)

print(f"Teddy is {random_num} years old")
