'''
11. Without running the following code, determin what each line should print
'''

print('johnson' in 'Joe Johnson')
print('sen' not in 'Joe Johnson')
print('Joe J' in 'Joe Johnson')
print(5 in range(5))
print(5 in range(6))
print(5 not in range(5, 10))
print(0 in range(10, 0, -1))
print(4 in {6, 5, 4, 3, 2, 1})
print({1, 2, 3} in {1, 2, 3})
print({3, 2} in {1, frozenset({2, 3})})

'''
False
True
True
False
True
False
False
True
False (This line is checking if there set is nest IN the set on the right which is is NOT)
True
'''
