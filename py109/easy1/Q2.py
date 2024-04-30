"""
Q2. Print all odd numbers from 1 to 99, inclusive, with each number on a seperate line

Bonus: Can you solve the problem by iterating over just the odd numbers?
"""

odd_numbers = [i for i in range(1, 100, 2)]

for number in odd_numbers:
    print(number)

"""
In this code example i used list comprehension to make the code very simple and concise

for within the `odd_numbers` list i am using a for loop 1-99 and if the conditional expression of checking if they are odd then it saves it to `i`

After that i used a for loop to iterate over the odd_numbers list and printed them individually
"""
