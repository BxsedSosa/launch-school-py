"""
4. Without running this code, what will in print? Why/
"""

dict1 = {
    "a": [1, 2, 3],
    "b": (4, 5, 6),
}

dict2 = dict(dict1)
dict1["a"][1] = 42
print(dict2["a"])

"""
[1, 42, 3]

This happens because its a nested list and its also mutable
"""
