'''
5. Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})
'''

'''
The range(5) wouldn't be able to be used because the range function is lazy and doesn't give you a valid object to be used as a key
'''

'''
Answer:

['a', 'b']
{'a': 1, 'b': 2}
{1, 4, 9, 16, 25}

Since these objects are mutable they can't be used as a dict key.
'''
