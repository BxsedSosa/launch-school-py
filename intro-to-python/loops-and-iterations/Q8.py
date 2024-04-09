"""
8. Write a comprehension that creates a dict, object whose key are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings 
"""

"""
The problem we are trying to solve is given a set of data we need to create a dict comprehension which the keys are the given strings in the set and the values are the lengths of how long they are. But only using the strings that have odd number length
"""

my_set = {
    "Fluffy",
    "Butterscotch",
    "Pudding",
    "Cheddar",
    "Cocoa",
}

odd_string = {f"{string}": len(string) for string in my_set if len(string) % 2 == 1}

print(odd_string)
