"""
Q1. Write two distinct ways of reversing the list without mutating the original list
"""

numbers = [1, 2, 3, 4, 5]

new_numbers = sorted(numbers, reverse=True)

another_new_numbers = list(reversed(numbers))

print("original")
print(numbers)
print("method 1")
print(new_numbers)
print("method 2")
print(another_new_numbers)
