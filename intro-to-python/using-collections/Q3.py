'''
3. Write python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverese order from the original. It should exclude the first and last members of the original. The result should be the tuple (4, 3, 2)
'''

tup = (1, 2, 3, 4, 5)
new_tup = reversed(tup[1: len(tup) - 1])
print(tuple(new_tup))

print(tup[-2: -5: -1])
