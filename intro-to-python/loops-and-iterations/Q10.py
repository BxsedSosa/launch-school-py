"""
10. The following code uses he randrange function from python's rnadom libaray to obtain and print a random integer within a given range. Using a while loop, it keeps running until it finds a random numebr that matches the last number in the range. Refactor the code so it doesn't require two different invocatinos of randrange.
"""

import random

highest = 10
number = random.randrange(highest + 1)
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)

print("--------------------------------")


def rand_num():
    highest = 10
    while True:
        number = random.randrange(highest + 1)
        print(number)
        if number == highest:
            break


rand_num()
